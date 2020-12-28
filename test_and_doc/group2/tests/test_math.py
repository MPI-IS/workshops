import random
from unittest import TestCase
from time import time

from sample_project.math import Sequence


class TestGeomean(TestCase):

    def setUp(self):
        seed = time()
        random.seed(seed)
        print(f"The seed for the RNG is {seed}")

    def tearDown(self):
        pass

    def test_toto(self):
        pass

    def test_geomean_basic(self):

        x = Sequence([7])
        self.assertEqual(x.geometric_mean(), 7)

        y = Sequence([7, 9, 1])
        self.assertEqual(y.geometric_mean(), 63 ** (1 / 3))

    def test_random(self):

        num_elems = random.randrange(10) + 1
        print("num_elems = ", num_elems)
        vals = []
        for _ in range(num_elems):
            vals.append(random.randrange(10))

        x = Sequence(vals)
        print("vals = ", vals)
        g_mean = x.geometric_mean()
        a_mean = x.arithmetic_mean()
        self.assertLessEqual(g_mean, a_mean)
