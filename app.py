from flask import Flask, request, jsonify, send_from_directory, redirect
from flask_cors import CORS
import os
import sqlite3
import random
import string

app = Flask(__name__)
CORS(app)

conn = sqlite3.connect('database.db', check_same_thread=False)  
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS urls (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code TEXT UNIQUE,
                    original_url TEXT
                )''')
conn.commit()

def random_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def salvar_url(url):
    while True:
        code = random_code()
        cursor.execute("SELECT 1 FROM urls WHERE code = ?", (code,))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO urls (code, original_url) VALUES (?, ?)", (code, url))
            conn.commit()
            return code

def buscar_url(code):
    cursor.execute("SELECT original_url FROM urls WHERE code = ?", (code,))
    result = cursor.fetchone()
    if result:
        return result[0]
    return None

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400
    url = data['url']
    if not url.startswith('http://') and not url.startswith('https://'):
        return jsonify({'error': 'Invalid URL'}), 400
    code = salvar_url(url)
    return jsonify({
        'code': code,
        'short_url': request.host_url + code
    })

@app.route('/<code>', methods=['GET'])
def redirect_to_url(code):
    url = buscar_url(code)
    if url:
        return redirect(url)
    else:
        return 'Not found', 404



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)