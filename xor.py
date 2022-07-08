import base64
import random
from hashlib import sha256


def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def cipher_encryption(msg, key):
    encrypt_hex = ""
    key_itr = 0
    for i in range(len(msg)):
        temp = ord(msg[i]) ^ ord(key[key_itr])
        encrypt_hex += hex(temp)[2:].zfill(2)
        key_itr += 1
        if key_itr >= len(key):
            key_itr = 0

    print("Encrypted Text: {}".format(encrypt_hex))


def cipher_decryption(msg, key):
    hex_to_uni = ""
    for i in range(0, len(msg), 2):
        hex_to_uni += bytes.fromhex(msg[i:i + 2]).decode('utf-8')

    decryp_text = ""
    key_itr = 0
    for i in range(len(hex_to_uni)):
        temp = ord(hex_to_uni[i]) ^ ord(key[key_itr])
        decryp_text += chr(temp)
        key_itr += 1
        if key_itr >= len(key):
            key_itr = 0

    print("Decrypted Text: {}".format(decryp_text))


class Cryptosystem:
    def __init__(self, elliptic_curve, point):
        self.ellipticCurve = elliptic_curve
        self.curve_point = point
        self.d = random.randint(2, self.ellipticCurve.n + 1)
        self.Q = self.curve_point * self.d

    def to_hash(self):
        self.hash = int(sha256(bytes(self.x, 'utf-8')).hexdigest(), 16)
        return self.hash

    def extract_keys(self):
        return [self.d, self.Q]

    def share_secret(self, public):
        return (public * self.d).Projective_To_Affine_Point()

    def wrap(key, shared_secret):
        c = cipher_encryption(int_to_bytes(shared_secret), key=key)
        return c

    def unwrap(encrypted_key, shared_secret):
        c = cipher_encryption(int_to_bytes(shared_secret), key=encrypted_key)
        return c



