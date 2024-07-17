def encrypt_symmetric_key(symmetric_key, public_key):
    rsa_cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    encrypted_key = rsa_cipher.encrypt(symmetric_key)
    return base64.b64encode(encrypted_key).decode('utf-8')

def decrypt_symmetric_key(encrypted_key, private_key):
    encrypted_key = base64.b64decode(encrypted_key.encode('utf-8'))
    rsa_cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
    symmetric_key = rsa_cipher.decrypt(encrypted_key)
    return symmetric_key
