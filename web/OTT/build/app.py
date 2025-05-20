from flask import Flask, jsonify, request
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os
import sqlite3
import json

# no front end just an api exactly what i love

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)

aes_key = get_random_bytes(16)

conn = sqlite3.connect('tokens.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS tokens (token TEXT UNIQUE NOT NULL)''')
conn.commit()
conn.close()

def encrypt(data):
    cipher = AES.new(aes_key, AES.MODE_GCM)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return base64.b64encode(nonce + ciphertext + tag).decode('utf-8')

def decrypt(encrypted_data):
    encrypted_data = base64.b64decode(encrypted_data)
    nonce = encrypted_data[:16]
    ciphertext = encrypted_data[16:-16]
    tag = encrypted_data[-16:]
    cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
    try:
        data = cipher.decrypt_and_verify(ciphertext, tag)
        return data.decode('utf-8')
    except ValueError:
        return None

def verify_token(token):
    conn = sqlite3.connect('tokens.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tokens WHERE token = ?', (token,))
    result = cursor.fetchone()
    if result:
        conn.close()
        return False
    
    else:
        decrypted_token = decrypt(token)
        if decrypted_token is None:
            return False
        
        if json.loads(decrypted_token)["VIP_token"] == True:
            cursor.execute('INSERT INTO tokens (token) VALUES (?)', (token,))
            conn.commit()
            conn.close()
            return True
        return False
    
@app.route('/flag')
def flag():
    if verify_token(request.cookies.get('token')):
        return jsonify({"flag": "defensys{take_care_of_base64_padding__98897314123}"})
    return jsonify({"flag": "You are not authorized to view this page!"})

@app.route('/health_check')
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/home')
def home():
    return jsonify({"message": "Welcome to the home page!"})

@app.route('/get_token')
def get_token():
    token = json.dumps({"username": "guest", "role": "guest", "VIP_token": True})
    encrypted_token = encrypt(token)
    response = jsonify({"message": "Congratulations! You have successfully obtained the token!"})
    response.set_cookie('token', encrypted_token)
    if not verify_token(encrypted_token):
        return jsonify({"message": "An error occurred!"})
    return response

@app.route('/verify_token', methods=['POST'])
def verify():
    token = request.cookies.get('token')
    if verify_token(token):
        return jsonify({"message": "Token is valid!"})
    else:
        return jsonify({"message": "Token is invalid!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)