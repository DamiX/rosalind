import os
import unittest as ut
from rosalind import io

print(os.getcwd())

class TestRosalindIO(ut.TestCase):
        def test_read_fasta(self):
                data = (">Rosalind_6404\n"
                        "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC\n"
                        "TCCCACTAATAATTCTGAGG\n"
                        ">Rosalind_5959\n"
                        "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT\n"
                        "ATATCCATTTGTCAGCAGACACGC\n"
                        ">Rosalind_0808\n"
                        "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC\n"
                        "TGGGAACCTGCGGGCAGTAGGTGGAAT\n")
                # with open("rosalind_fasta_test.txt", 'w') as f:
                #         f.write(data)
                # print(data)

if __name__ == "__main__":
        suite = ut.TestLoader().loadTestsFromTestCase(TestRosalindIO)
        ut.TextTestRunner(verbosity=2).run(suite)