from flask import Flask, request, jsonify, session
import mysql.connector
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt
from flask_session import Session
import jwt
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime, timedelta
import os
import logging




app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
app.secret_key = os.urandom(24)
logging.basicConfig(level=logging.INFO)

app.config['SESSION_TYPE'] = 'filesystem'  # Verwenden Sie die Dateisystem-Sitzungsspeicherung
app.config['SESSION_PERMANENT'] = False     # Sitzungen verfallen nach Schließen des Browsers
app.config['SESSION_USE_SIGNER'] = True     # Sitzungsdaten signieren
app.config['SESSION_KEY_PREFIX'] = 'myapp_' # Präfix für Sitzungsschlüssel



db = mysql.connector.connect(
    host = 'localhost',
    user = 'mamp',
    password = 'root',
    database = 'mydb',
    port = 8889
)

cursor = db.cursor()

salt = "fridolin"

app.config['SECRET_KEY'] = 'totalGeheimerSchluessel'

def generate_jwt_token(user_id):
    expiration = datetime.utcnow() + timedelta(hours=1)
    payload = {'user_id': user_id, 'exp': expiration}
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    app.logger.info(f"Token für Benutzer {user_id} generiert")
    return token


@app.route('/add_user', methods=['POST'])
@cross_origin(origin='http://localhost:5173', supports_credentials=True)
def add_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s",(username,))
    existing_user = cursor.fetchone()[0]

    if existing_user > 0:
        return jsonify({"messageUser": "Der Benutzername ist schon vorhanden"})


    hashed_password = bcrypt.generate_password_hash(password + salt).decode('utf-8')

    insert_query = "INSERT INTO users (username, hashed_password, salt) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (username, hashed_password, salt))
    db.commit()

    return jsonify({"message" : "Die Registrierung war erfolgreich!"})

@app.route('/login', methods=['POST'])
@cross_origin(origin='http://localhost:5173', supports_credentials=True)
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    cursor.execute("SELECT id, hashed_password, salt FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result is not None:
        user_id, stored_hashed_password, stored_salt = result

        if bcrypt.check_password_hash(stored_hashed_password, password + stored_salt):
            token = generate_jwt_token(user_id)
            app.logger.info(f"Token für Benutzer {username} generieet: {token}")

        
            session['logged_in'] = True
            return jsonify({"message": "Erfolgreich eingeloggt", "token": token})
            
    return jsonify({"message": "Anmeldung fehlgeschlagen"})

def userInfo():
    current_user = get_jwt_identity()
    cursor.execute("SELECT username FROM users WHERE id = %s", (current_user,))
    result = cursor.fetchone()
    if result:
        username = result[0]
        return jsonify(username=username), 200
    else:
        return jsonify(message="Benutzer nicht gefunden"), 400
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

#app.logger.info("Noch eine Log-Meldung")
#app.logger.error("Das ist ein Fehler")

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({"message" : "Erfolgreich ausgeloggt"})

if __name__ == '__main__':
    Session(app)
    app.run(debug=True)
