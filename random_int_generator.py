import numpy as np
import secrets
import hmac
import hashlib

class RandomIntGenerator:
    def __init__(self, range):
        self.range = range
        self.num = self.generate_random_uniform_int()
        self.key = self.generateKey()
        self.hmac = self.generate_hmac()

    def generate_random_uniform_int(self):
        return int(np.random.uniform(low=0, high=self.range))
    
    def generateKey(self):
        return secrets.token_hex(32)

    def generate_hmac(self):
        key = self.key.encode()
        message = str(self.num).encode()
        h = hmac.new(key, message, hashlib.sha3_256)
        return h.hexdigest()