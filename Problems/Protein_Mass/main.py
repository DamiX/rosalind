import sys
import argparse

monoisotopic_mass_table = {
        "A": 71.03711,
        "C": 103.00919,
        "D": 115.02694,
        "E": 129.04259,
        "F": 147.06841,
        "G": 57.02146,
        "H": 137.05891,
        "I": 113.08406,
        "K": 128.09496,
        "L": 113.08406,
        "M": 131.04049,
        "N": 114.04293,
        "P": 97.05276,
        "Q": 128.05858,
        "R": 156.10111,
        "S": 87.03203,
        "T": 101.04768,
        "V": 99.06841,
        "W": 186.07931,
        "Y": 163.06333
}

def compute_protein_mass(p):
        """
        Compute the total weight of a given protein string

        :param p -- protein string
        """
        p = p.upper()
        return sum([monoisotopic_mass_table[x] for x in p])

def main():
        # Setup parser
        parser = argparse.ArgumentParser(description="Count DNA Nucleotides")
        parser.add_argument("input_file", help="Input file containing k-mers input")
        parser.add_argument("-p", "--precision", help="Percision", type=int, default="3")
        parser.add_argument("-o", "--output_file", help="Output file containing the result", action="store_true", required=False)
        args = parser.parse_args()

        with open(args.input_file, 'r') as f:
                protein_string = f.read()

        weight = compute_protein_mass(protein_string.strip('\n'))
        weight = round(weight, args.precision)

        if args.output_file:
                with open("results.txt", 'w') as output:
                        output.write(str(weight))
        else:
                print(weight)

if __name__ == "__main__":
        main()