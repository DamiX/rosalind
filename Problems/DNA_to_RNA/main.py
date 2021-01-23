import argparse
from rosalind.algorithm import DNA_to_RNA

def main():
        parser = argparse.ArgumentParser(description="Transcribe DNA into RNA")
        parser.add_argument("input_file", help="Input file")
        parser.add_argument("-o", "--output_file", help="Output file", action="store_true", required=False)
        args = parser.parse_args()

        with open(args.input_file, 'r') as f:
                dna_string = f.read()

        rna_string = DNA_to_RNA(dna_string)

        if args.output_file:
                with open("results.txt", 'w') as output:
                        output.write(rna_string)
        else:
                print(rna_string)

if __name__ == "__main__":
        main()