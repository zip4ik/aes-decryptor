from flask import Flask, request, jsonify
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64

app = Flask(_name)  # правильно: __name_, а не name

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.get_json()
        key = base64.b64decode(data.get('key'))
        nonce = base64.b64decode(data.get('nonce'))
        ciphertext = base64.b64decode(data.get('ciphertext'))

        aesgcm = AESGCM(key)
        plaintext = aesgcm.decrypt(nonce, ciphertext, None)

        return jsonify({"plaintext": plaintext.decode("utf-8")})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# И это тоже: _name_ == '_main_'
if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
