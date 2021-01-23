import unittest as ut
from rosalind import transform

class TestRosalindTransform(ut.TestCase):
        def test_reverse_complement(self):
                data = "AAAACCCGGT"
                expected = "ACCGGGTTTT"
                self.assertEqual(expected, transform.reverse_complement(data))

        def test_dna_to_rna(self):
                data = "GATGGAACTTGACTACGTAAATT"
                expected = "GAUGGAACUUGACUACGUAAAUU"
                self.assertEqual(expected, transform.DNA_to_RNA(data))

        def test_rna_to_protein(self):
                data = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
                result = "MAMAPRTEINSTRING"
                self.assertEqual(transform.RNA_to_PROTEIN(data), result)

if __name__ == "__main__":
        suite = ut.TestLoader().loadTestsFromTestCase(TestRosalindTransform)
        ut.TextTestRunner(verbosity=2).run(suite)