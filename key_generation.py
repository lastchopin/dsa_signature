import random
from Crypto.Util import number
from sympy import mod_inverse, isprime


def generate_large_prime(bits):
    while True:
        prime_candidate = number.getPrime(bits)
        if isprime(prime_candidate):
            return prime_candidate


def generate_rsa_key(bits):
    p = generate_large_prime(bits // 2)
    q = generate_large_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2 ** 16 + 1
    while number.GCD(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d = mod_inverse(e, phi)
    return p, q, n, phi, e, d


if __name__ == "__main__":
    bits = 3000
    p, q, n, phi, e, d = generate_rsa_key(bits)
    with open('rsa_key.txt', 'w') as f:
        f.write(f"p: {p}\nq: {q}\nn: {n}\nφ(n): {phi}\ne: {e}\nd: {d}")
    print("RSA-Schlüssel generiert und in rsa_key.txt gespeichert.")
