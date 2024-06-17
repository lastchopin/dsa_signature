import random
import hashlib
from sympy import mod_inverse


def sha256_hash(message):
    return int(hashlib.sha256(message).hexdigest(), 16)


def dsa_sign(message, p, q, g, a, r=None):
    if r is None:
        r = random.randint(1, q - 1)
    gamma = pow(g, r, p) % q
    r_inv = mod_inverse(r, q)
    message_hash = sha256_hash(message)
    delta = (r_inv * (message_hash + a * gamma)) % q
    return gamma, delta, r


def recover_private_key(gamma, delta1, delta2, hash1, hash2, q):
    delta1_inv = mod_inverse(delta1, q)
    delta2_inv = mod_inverse(delta2, q)
    num = (hash2 * delta2_inv - hash1 * delta1_inv) % q
    denom = (gamma * (delta1_inv - delta2_inv)) % q
    denom_inv = mod_inverse(denom, q)
    a = (num * denom_inv) % q
    return a


if __name__ == "__main__":
    # Lade die Schlüsselparameter
    with open('dsa_keys.txt', 'r') as f:
        keys = f.read().split('\n')
        p = int(keys[0].split(': ')[1])
        q = int(keys[1].split(': ')[1])
        g = int(keys[2].split(': ')[1])
        a = int(keys[3].split(': ')[1])
        beta = int(keys[4].split(': ')[1])

    # Zwei Beispielnachrichten
    message1 = b'Erste Nachricht zur Signatur'
    message2 = b'Zweite Nachricht zur Signatur'

    # Signaturerstellung mit der gleichen Zufallszahl r
    gamma1, delta1, r1 = dsa_sign(message1, p, q, g, a, r=12345)
    gamma2, delta2, r2 = dsa_sign(message2, p, q, g, a, r=r1)

    # Hash-Werte der Nachrichten
    hash1 = sha256_hash(message1)
    hash2 = sha256_hash(message2)

    # Berechne den privaten Schlüssel a aus den Signaturen
    recovered_a = recover_private_key(gamma1, delta1, delta2, hash1, hash2, q)

    # Speichere die Ergebnisse in einer Datei
    with open('dsa_attack_results.txt', 'w') as f:
        f.write(f'Signatur 1: (gamma: {gamma1}, delta: {delta1})\n')
        f.write(f'Signatur 2: (gamma: {gamma2}, delta: {delta2})\n')
        f.write(f'Berechneter privater Schlüssel: {recovered_a}\n')
        f.write(f'Echter privater Schlüssel: {a}\n')
        f.write(f'Schlüssel stimmen überein: {recovered_a == a}\n')

    print(f"Berechneter privater Schlüssel: {recovered_a}")
    print(f"Echter privater Schlüssel: {a}")
    print(f"Schlüssel stimmen überein: {recovered_a == a}")
