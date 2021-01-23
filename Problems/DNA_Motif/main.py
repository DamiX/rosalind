import argparse
from rosalind.algorithm import substring

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Find a motif in DNA")
        parser.add_argument("input_file", help="Input file")
        parser.add_argument("-o", "--output_file", help="Output file", action="store_true")
        args = parser.parse_args()

        with open(args.input_file, 'r') as f:
                content = [s.strip() for s in f.readlines()]

        dna, motif = content
        res = substring(dna, motif)

        if args.output_file:
                with open("result.txt", 'w') as output:
                        output.write(' '.join([str(i) for i in res]))
        else:
                print(' '.join([str(i) for i in res]))