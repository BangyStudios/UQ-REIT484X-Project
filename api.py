from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
from pymysql.cursors import DictCursor

app = Flask(__name__)
CORS(app)

"""MySQL Configuration"""
db_host = "au1-1.edge.icbix.com"
db_user = "fbinsect"
db_password = "fbinsect"
db_name = "fbinsect"

@app.route("/stats/all", methods=["GET"])
def get_stats_all():
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

@app.route("/stats/last/<int:n_last>", methods=["GET"])
def get_stats_last(n_last):
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

@app.route("/stats/count", methods=["GET"])
def get_stats_count():
    db_connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name, cursorclass=DictCursor)
    db_cursor = db_connection.cursor()
    db_cursor.execute("""
        SELECT COUNT(*) FROM stats;             
    """)
    rows = db_cursor.fetchall()
    db_cursor.close()
    db_connection.close()
    return jsonify(rows)

@app.route('/stats/add', methods=['POST'])
def insert_probabilities():
    # Retrieve probabilities from request
    probabilities = request.json.get('probabilities')

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
    app.run(port="5001", debug=True)