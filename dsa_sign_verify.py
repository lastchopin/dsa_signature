import hashlib
import random
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


def dsa_verify(message, gamma, delta, p, q, g, beta):
    if not (0 < gamma < q and 0 < delta < q):
        return False
    delta_inv = mod_inverse(delta, q)
    message_hash = sha256_hash(message)
    e1 = (message_hash * delta_inv) % q
    e2 = (gamma * delta_inv) % q
    v = (pow(g, e1, p) * pow(beta, e2, p) % p) % q
    return v == gamma


if __name__ == "__main__":
    # Lade die Schlüsselparameter
    with open('dsa_keys.txt', 'r') as f:
        keys = f.read().split('\n')
        p = int(keys[0].split(': ')[1])
        q = int(keys[1].split(': ')[1])
        g = int(keys[2].split(': ')[1])
        a = int(keys[3].split(': ')[1])
        beta = int(keys[4].split(': ')[1])

    # Wähle eine Nachricht
    message = b'Beispielnachricht zur Signatur'

    # Signiere die Nachricht
    gamma, delta, r = dsa_sign(message, p, q, g, a)

    # Verifiziere die Signatur
    valid = dsa_verify(message, gamma, delta, p, q, g, beta)

    # Speichere die Signatur
    with open('signature.txt', 'w') as f:
        f.write(f"gamma: {gamma}\ndelta: {delta}")

    print("Nachricht signiert und in signature.txt gespeichert.")

    # Speichere die Ergebnisse in einer Datei
    with open('dsa_sign_verify_results.txt', 'w') as f:
        f.write(f'Nachricht: {message.decode()}\n')
        f.write(f'Signatur: (gamma: {gamma}, delta: {delta})\n')
        f.write(f'Signatur gültig: {valid}\n')

    print(f"Signatur gültig: {valid}")
