from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host = 'localhost',
    user = 'mamp',
    password = 'root',
    database = 'mydb',
    port = 8889
)

cursor = db.cursor()

@app.route('/add_user', methods=['POST'])
@cross_origin(origin='http://localhost:5173', supports_credentials=True)
def add_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(insert_query, (username, password))
    db.commit()

    return jsonify({"message" : "Benutzer wurde hinzugefuegt"})

if __name__ == '__main__':
    app.run(debug=True)
