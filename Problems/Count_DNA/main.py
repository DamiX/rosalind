import argparse

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Count DNA Nucleotides")
        parser.add_argument("input_file", help="Input file")
        parser.add_argument("-o", "--output_file", help="Output file", action="store_true", required=False)
        args = parser.parse_args()

        with open(args.input_file, 'r') as f:
                dna_string = f.read()

        counter = map(dna_string.count, "ACGT")

        if args.output_file:
                with open("result.txt", 'w') as output:
                    output.write(' '.join([str(v) for v in counter]))
        else:
                print(' '.join([str(v) for v in counter]))