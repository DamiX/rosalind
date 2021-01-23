import sys
import argparse

def enum_kmers(alphabet, n):
        """


        :param alphabet -- symbols defining an ordered alphabet
        :param n        -- positive integer, length of enumerate string
        """
        assert(n > 0)
        assert(len(alphabet) >= 1)

        def recursion(s, n):
                if n == 0:
                        return s
                else:
                        

def main():
        # Setup parser
        parser = argparse.ArgumentParser(description="Count DNA Nucleotides")
        parser.add_argument("input_file", help="Input file containing k-mers input")
        parser.add_argument("-o", "--output_file", help="Output file containing the result", action="store_true", required=False)
        args = parser.parse_args()

        with open(args.input_file, 'r') as f:
                content = f.readlines()
        inputs = [c.strip() for c in content]

        # Setup input for enum_kmers
        n = inputs[1]
        alphabet = list(inputs[0].replace(' ', ''))

        res = enum_kmers(alphabet, n)

        if args.output_file:
                with open("results.txt", 'w') as output:
                        output.write('\n'.join([str(i) for i in perm]))
        else:
                print('\n'.join([str(i) for i in perm]))

if __name__ == "__main__":
        main()