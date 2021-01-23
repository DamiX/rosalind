import argparse
from rosalind import transform

if __name__ == "__main__":
        # Setup parser
        parser = argparse.ArgumentParser(description="Count DNA Nucleotides")
        parser.add_argument("input_file", help="Input file containing k-mers input")
        parser.add_argument("-o", "--output_file", help="Output file containing the result", action="store_true", required=False)
        args = parser.parse_args()

        with open(args.input_file, 'r') as f:
                rna = f.readlines()[0]

        protein = transform.RNA_to_PROTEIN(rna.strip('\n'))

        if args.output_file:
                with open("results.txt", 'w') as output:
                        output.write(protein)
        else:
                print(protein)