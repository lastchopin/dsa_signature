import random
from Crypto.Util import number
from sympy import mod_inverse, isprime


def generate_prime(bits):
    return number.getPrime(bits)


def generate_dsa_keys():
    # Schritt 1: Wähle zwei Primzahlen p und q
    q = generate_prime(256)

    # Finde eine 3072-Bit Primzahl p, so dass q ein Primzahlfaktor von p-1 ist
    while True:
        k = number.getRandomNBitInteger(3072 - 256)
        p = q * k + 1
        if isprime(p):
            break

    # Schritt 2-4: Bestimmen des Generators alpha
    e = (p - 1) // q
    while True:
        h = random.randint(2, p - 2)
        g = pow(h, e, p)
        if g != 1:
            break

    # Schritt 5: Wähle eine Zahl a zufällig und berechne beta
    a = random.randint(1, q - 1)
    beta = pow(g, a, p)

    return p, q, g, a, beta


if __name__ == "__main__":
    # Generiere DSA-Schlüssel
    p, q, g, a, beta = generate_dsa_keys()

    # Speichere die Schlüssel in einer Datei
    with open('dsa_keys.txt', 'w') as f:
        f.write(f"p: {p}\nq: {q}\ng: {g}\na (private key): {a}\nbeta: {beta}")

    print("DSA-Schlüssel generiert und in dsa_keys.txt gespeichert.")
