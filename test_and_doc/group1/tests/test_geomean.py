import random
import time
from unittest import TestCase

from sample_project.geomean import calculate_geomean


class TestGeomean(TestCase):

    def setUp(self):

        current_time = time.time()
        random.seed(current_time)
        print("RNG seed is current time = {}".format(current_time))

    def test_calculate_geomean(self):

        seq = [7]
        self.assertEqual(calculate_geomean(seq), 7)
        seq = [2, 2]
        self.assertEqual(calculate_geomean(seq), 2)
        seq = [1, 2, 7]
        self.assertEqual(calculate_geomean(seq), 14 ** (1 / 3))

    def test_random(self):

        num_elements = random.randrange(10) + 2
        seq = []
        for i in range(1, num_elements):
            seq.append(i)
        g_mean = calculate_geomean(seq)
        self.assertGreater(g_mean, 0)

        # Check w.r.t. arithmetic mean
        a_mean = sum(seq) / len(seq)
        self.assertLessEqual(g_mean, a_mean)

    def test_string(self):
        seq = 'toto'
        with self.assertRaises(TypeError):
            calculate_geomean(seq)

    def test_negative(self):
        seq = [1, 2, -3]
        with self.assertRaises(TypeError):
            calculate_geomean(seq)

    def test_empty_seq(self):
        with self.assertRaises(ValueError):
            calculate_geomean([])
