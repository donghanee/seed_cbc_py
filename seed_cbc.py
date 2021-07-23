"""
KISA Seed CBC
"""

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import SEED
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.backends.openssl.backend import backend
import base64


class SeedCBC:
    def __init__(self, key, iv) -> None:
        self.key = key
        self.iv = iv
        self.cipher = Cipher(
            SEED(self.key.encode()),
            CBC(self.iv.encode()),
            backend
        )

    def Encrypt(self, s):
        s = self.pad(s)
        encryptor = self.cipher.encryptor()
        enc = encryptor.update(s.encode()) + encryptor.finalize()
        enc = base64.b64encode(enc).decode()
        return enc

    def Decrypt(self, s):
        s = base64.b64decode(s)
        decryptor = self.cipher.decryptor()
        enc = decryptor.update(s) + decryptor.finalize()
        return self.unpad(enc.decode())

    def pad(self, s):
        BLOCK_SIZE = 16
        return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

    def unpad(self, s):
        i = s.find('\x00')
        if i != -1:
            return s[:i]
        i = s.find('\x06')
        if i != -1:
            return s[:i]
        i = s.find('\x10')
        if i != -1:
            return s[:i]
        return s
