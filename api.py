from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
from pymysql.cursors import DictCursor
from datetime import datetime, timedelta
from pytz import timezone

app = Flask(__name__)
CORS(app)

"""MySQL Configuration"""
db_host = "localhost"
db_user = "fbinsect"
db_password = "fbinsect"
db_name = "fbinsect"

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

@app.route('/api/add', methods=['POST'])
def insert_probabilities():
    # Retrieve probabilities from request
    probabilities = request.json.get('probabilities')
    print(probabilities, type(probabilities))

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

if (__name__ == "__main__"):
    app.run(port="5001", debug=True) # host="0.0.0.0"