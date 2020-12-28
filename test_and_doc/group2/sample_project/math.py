class Sequence:

    def __init__(self, seq):
        self.data = list(seq)

    def arithmetic_mean(self):
        return sum(self.data) / len(self.data)

    def geometric_mean(self):

        n = len(self.data)

        if not n:
            raise ValueError("There should be at least one element in the data.")

        assert n > 0, "Bad bad..."

        product = 1
        for e in self.data:
            product *= e
        return product ** (1 / n)
