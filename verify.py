import hashlib


def sha256_hash(message):
    return int(hashlib.sha256(message).hexdigest(), 16)


def rsa_verify(message, signature, e, n):
    message_hash = sha256_hash(message)
    return pow(signature, e, n) == message_hash


if __name__ == "__main__":
    with open('rsa_key.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[2].split(": ")[1])
        e = int(lines[4].split(": ")[1])

    with open('signature.txt', 'r') as f:
        lines = f.readlines()
        message = lines[0].split(": ")[1].strip().encode()
        signature = int(lines[1].split(": ")[1])

    is_valid = rsa_verify(message, signature, e, n)
    print(f"Signatur gültig: {is_valid}")
