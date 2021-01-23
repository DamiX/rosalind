import argparse
from rosalind.transform import reverse_complement

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Reverse complement a DNA string")
        parser.add_argument("input_file", help="Input file containing a DNA string")
        parser.add_argument("-o", "--output_file", help="Output file which will hold the result", action="store_true", required=False)
        args = parser.parse_args()

        with open(args.input_file, 'r') as f:
                dna_string = f.read().strip()

        res = reverse_complement(dna_string)

        if args.output_file:
                with open("result.txt", 'w') as output:
                        output.write(res)
        else:
                print(res)