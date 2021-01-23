import main
import unittest as ut

class TestSharedMotif(ut.TestCase):
        def test_generate_substring(self):
                input="ATACA"
                data = {
                        5: ["ATACA"],
                        4: ["ATAC", "TACA"],
                        3: ["ATA", "TAC", "ACA"],
                        2: ["AT", "TA", "AC", "CA"],
                        1: ["A", "T", "C"]
                }

                i = len(input)
                while i > 0:
                        substring = main.generate_substring(input, i)
                        self.assertEqual(substring, data[i])
                        i -= 1

if __name__ == "__main__":
        suite = ut.TestLoader().loadTestsFromTestCase(TestSharedMotif)
        ut.TextTestRunner(verbosity=2).run(suite)