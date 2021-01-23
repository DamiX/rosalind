import main
import unittest as ut

class TestProteinMass(ut.TestCase):
        def test_compute_protein_mass(self):
                input = "SKADYEK"
                result = 821.392
                self.assertEqual(round(main.compute_protein_mass(input), 3), result)

if __name__ == "__main__":
        suite = ut.TestLoader().loadTestsFromTestCase(TestProteinMass)
        ut.TextTestRunner(verbosity=2).run(suite)