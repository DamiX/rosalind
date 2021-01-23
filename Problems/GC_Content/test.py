import main
import unittest as ut

class TestGCContent(ut.TestCase):
        def test_compute_gc_content(self):
                input = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
                result = 60.919540
                computed = main.compute_gc_content(input)
                self.assertEqual(round(computed, 6), result)
                self.assertLessEqual(abs(computed-result), 0.001)

if __name__ == "__main__":
        suite = ut.TestLoader().loadTestsFromTestCase(TestGCContent)
        ut.TextTestRunner(verbosity=2).run(suite)