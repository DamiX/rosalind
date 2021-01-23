import unittest as ut
from rosalind import algorithm

class TestRosalindAlgorithm(ut.TestCase):
        def test_substring(self):
                data  = "GATATATGCATATACTT"
                motif = "ATAT"
                expected = [2, 4, 10]
                self.assertEqual(expected, algorithm.substring(data, motif))

        def test_hamming_distance(self):
                data1 = "GAGCCTACTAACGGGAT"
                data2 = "CATCGTAATGACGGCCT"
                expected = 7
                self.assertEqual(expected, algorithm.hamming_distance(data1, data2))

if __name__ == "__main__":
        suite = ut.TestLoader().loadTestsFromTestCase(TestRosalindAlgorithm)
        ut.TextTestResult(verbosity=2).run(suite)