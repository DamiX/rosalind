import sys
import argparse
from rosalind import algorithm

if __name__ == "__main__":
        # Setup parser
        parser = argparse.ArgumentParser(description="Count point mutations")
        parser.add_argument("input_file", help="Input file")
        parser.add_argument("-o", "--output_file", help="Output file", action="store_true", required=False)
        args = parser.parse_args()

        with open(args.input_file, 'r') as f:
                content = [s.strip() for s in f.readlines()]
        if len(content) != 2:
                sys.exit()

        dna1, dna2 = content

        # Compute hamming distance
        try:
                dist = hamming_distance(dna1, dna2)
        except ValueError as e:
                print(e)
                sys.exit(1)

        if args.output_file:
                with open("results.txt", 'w') as output:
                        output.write(dist)
        else:
                print(dist)