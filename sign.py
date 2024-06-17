import hashlib
from sympy import mod_inverse

def sha256_hash(message):
    return int(hashlib.sha256(message).hexdigest(), 16)

def rsa_sign(message, d, n):
    message_hash = sha256_hash(message)
    return pow(message_hash, d, n)

if __name__ == "__main__":
    message = b'Example message for signing'
    with open('rsa_key.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[2].split(": ")[1])
        d = int(lines[5].split(": ")[1])
    signature = rsa_sign(message, d, n)
    with open('signature.txt', 'w') as f:
        f.write(f"Message: {message.decode()}\nSignature: {signature}")
    print("Nachricht signiert und in signature.txt gespeichert.")
