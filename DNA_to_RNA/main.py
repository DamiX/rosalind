import argparse

def main():
        # Setup parser
        parser = argparse.ArgumentParser(description="Count DNA Nucleotides")
        parser.add_argument("input_file", help="Input file containing a DNA string")
        parser.add_argument("-o", "--output_file", help="Output file containing the result", action="store_true", required=False)
        args = parser.parse_args()

        with open(args.input_file, 'r') as f:
                dna_string = f.read()

        rna_string = dna_string.replace('T', 'U')

        if args.output_file:
                with open("results.txt", 'w') as output:
                        output.write(rna_string)
        else:
                print(rna_string)

if __name__ == "__main__":
        main()