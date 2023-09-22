from flask import Flask, request
import mysql.connector
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 8889
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'LernApp'

mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    port=app.config['MYSQL_PORT'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

@app.route('/register', methods=['POST'])
def register():
    try:
        username = request.json['username']
        password = request.json['password']

        print(f"Received registration request for username: {username}")

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO login (username, password) VALUES (%s, %s)", (username, password))
        cursor.close()

        return 'Registrierung erfolgreich', 200
    except Exception as e:
        print(f"Error during registration: {str(e)}")
        return str(e), 400


if __name__ == '__main__':
    app.run(port=8889)
