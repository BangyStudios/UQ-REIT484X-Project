import config as conf
import pipeline

from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
from pymysql.cursors import DictCursor
from datetime import datetime, timedelta
from pytz import timezone
import threading
import os

app = Flask(__name__)
CORS(app)

config = conf.get_config()
pipeline = pipeline.Pipeline()

# Flask configuration
host = config.get("rpi").get("api_host")
port = config.get("rpi").get("api_port")
debug = config.get("rpi").get("api_debug")
db_host = config.get("rpi").get("api_db_host")
db_user = config.get("rpi").get("api_db_user")
db_password = config.get("rpi").get("api_db_password")
db_name = config.get("rpi").get("api_db_name")

# Get events endpoints

@app.route("/api/all", methods=["GET"])
def get_events_all():
    db_connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name, cursorclass=DictCursor)
    db_cursor = db_connection.cursor()
    db_cursor.execute("""
        SELECT * FROM stats 
        ORDER BY timestamp DESC;
    """)
    rows = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return jsonify(rows)

@app.route("/api/last/<int:n_last>", methods=["GET"])
def get_events_last(n_last):
    db_connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name, cursorclass=DictCursor)
    db_cursor = db_connection.cursor()
    db_cursor.execute("""
        SELECT * FROM stats 
        ORDER BY timestamp DESC 
        LIMIT %s;                  
    """, (n_last,))
    rows = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return jsonify(rows)

@app.route("/api/timelast/<string:range_time>", methods=["GET"])
def get_events_timelast(range_time):
    # Mapping of range_time to timedelta values
    time_delta_map = {
        "5m": timedelta(minutes=5),
        "15m": timedelta(minutes=15),
        "1h": timedelta(hours=1)
    }

    if range_time not in time_delta_map:
        return jsonify({"error": "Invalid range_time"}), 400

    time_delta = time_delta_map[range_time]
    aest = timezone ("Australia/Brisbane")
    time_threshold = datetime.now(aest) - time_delta

    db_connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name, cursorclass=DictCursor)
    db_cursor = db_connection.cursor()
    db_cursor.execute("""
        SELECT * FROM stats 
        WHERE timestamp >= %s
        ORDER BY timestamp DESC;                  
    """, (time_threshold,))
    rows = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return jsonify(rows)

# Delete events endpoint

@app.route("/api/prune/<int:n_last>", methods=["GET"])
def prune_events_last(n_last):
    db_connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name, cursorclass=DictCursor)
    db_cursor = db_connection.cursor()
    
    # Get the timestamp of the nth last entry
    db_cursor.execute("""
        SELECT timestamp FROM stats
        ORDER BY timestamp DESC
        LIMIT 1 OFFSET %s;
    """, (n_last-1,))
    
    row = db_cursor.fetchone()
    if row is None:
        db_cursor.close()
        db_connection.close()
        return jsonify({"message": "Insufficient data points"}), 400
    
    nth_timestamp = row["timestamp"]
    
    # Delete all entries older than nth_timestamp
    db_cursor.execute("""
        DELETE FROM stats
        WHERE timestamp < %s;
    """, (nth_timestamp,))
    
    db_connection.commit()
    db_cursor.close()
    db_connection.close()
    
    return jsonify({"message": "Pruned successfully"}), 200

# Get event counts endpoints

@app.route("/api/count/events", methods=["GET"])
def get_count_events():
    db_connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name, cursorclass=DictCursor)
    db_cursor = db_connection.cursor()
    db_cursor.execute("""
        SELECT COUNT(DISTINCT timestamp) FROM stats;           
    """)
    rows = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return jsonify(rows)

@app.route("/api/count/datapoints", methods=["GET"])
def get_count_datapoints():
    db_connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name, cursorclass=DictCursor)
    db_cursor = db_connection.cursor()
    db_cursor.execute("""
        SELECT COUNT(*) FROM stats;           
    """)
    rows = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return jsonify(rows)

@app.route("/api/count/probability", methods=["GET"])
def get_total_probability():
    db_connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name, cursorclass=DictCursor)
    db_cursor = db_connection.cursor()
    
    # Initialize class probabilities
    classes = config.get("train").get("n_class")
    class_probabilities = {c: 0.0 for c in range(classes)}

    # Execute SQL query
    db_cursor.execute("SELECT class, probability FROM stats;")
    rows = db_cursor.fetchall()

    # Sum probabilities for each class
    for row in rows:
        class_id = row["class"]
        probability = row["probability"]
        class_probabilities[class_id] += probability

    # Close database connections
    db_cursor.close()
    db_connection.close()
    
    print(class_probabilities)

    return jsonify(class_probabilities)

# Insert endpoints

@app.route("/api/add", methods=["POST"])
def insert_probabilities():
    # Retrieve probabilities from request
    probabilities = request.json.get("probabilities")

    if not probabilities or not all(isinstance(prob, (float, int)) for prob in probabilities):
        return jsonify({"error": "Invalid probabilities"}), 400

    # Connect to the database
    db_connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name, cursorclass=DictCursor)
    db_cursor = db_connection.cursor()

    try:
        # Insert each probability into the stats table with its corresponding class_id
        for class_id, probability in enumerate(probabilities):
            db_cursor.execute("INSERT INTO stats (class, probability) VALUES (%s, %s);", (class_id, probability))
        
        # Commit the transaction
        db_connection.commit()

        return jsonify({"message": "Inserted successfully!"}), 201

    except pymysql.MySQLError as e:
        # Handle any MySQL error
        return jsonify({"error": "Failed to insert into the database."}), 500

    finally:
        # Close the cursor and connection
        db_cursor.close()
        db_connection.close()
        
# Pipeline endpoints

@app.route("/api/pipeline/start")
def pipeline_start():
    pipeline.exit = False
    pipeline_thread = threading.Thread(target=pipeline.run)
    pipeline_thread.start()
    return "Pipeline started..."

@app.route("/api/pipeline/stop")
def pipeline_stop():
    pipeline.exit = True
    return "Pipeline stopped..."

@app.route("/api/pipeline/delay/<int:length_delay>", methods=["GET"])
def pipeline_delay(length_delay):
    pipeline.run_delay = length_delay
    return f"Pipeline delay set to {length_delay} seconds..."

# File endpoints

@app.route("/api/rpi/receive", methods=["post"])
def rpi_receive():
    received_file = request.files["file"]
    received_path = request.form.get("path", "")
    if not os.path.exists(received_path):
        os.makedirs(received_path)
    if (received_file.filename != ""):
        path_file = os.path.join(received_path, received_file.filename)
        received_file.save(path_file)
        return f"File {received_file.filename} uploaded successfully.", 200
    else:
        return "No file selected", 400

if (__name__ == "__main__"):
    app.run(host=host, port=port, debug=debug) # host="0.0.0.0"