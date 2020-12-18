class Sequence:

    def __init__(self, seq):
        self.data = list(seq)

    def arithmetic_mean(self):
        return sum(self.data) / len(self.data)
