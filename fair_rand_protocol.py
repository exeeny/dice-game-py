class FairRandProtocol:
    def __init__(self, a, b, length):
        self.a = a
        self.b =b
        self.modulo_base = length

    def calculate_index(self):
        return (self.a + self.b) % self.modulo_base