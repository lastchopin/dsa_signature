import hashlib
import random
from sympy import mod_inverse


def sha256_hash(message):
    return int(hashlib.sha256(message).hexdigest(), 16)


def universal_forgery_attack(message, e, d, n):
    while True:
        r = random.randint(2, n - 1)
        if pow(r, e, n) != 1:
            break
    message_hash = sha256_hash(message)
    m_prime = (pow(r, e, n) * message_hash) % n
    s_prime = pow(m_prime, d, n)
    r_inv = mod_inverse(r, n)
    s = (r_inv * s_prime) % n
    return s


if __name__ == "__main__":
    with open('rsa_key.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[2].split(": ")[1])
        e = int(lines[4].split(": ")[1])
        d = int(lines[5].split(": ")[1])

    message = b'Example message for forgery'
    forged_signature = universal_forgery_attack(message, e, d, n)

    with open('forged_signature.txt', 'w') as f:
        f.write(f"Message: {message.decode()}\nForged Signature: {forged_signature}")
    print("Gefälschte Signatur erstellt und in forged_signature.txt gespeichert.")

    is_valid = pow(forged_signature, e, n) == sha256_hash(message)
    print(f"Gefälschte Signatur gültig: {is_valid}")
