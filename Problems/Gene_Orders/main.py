import sys
import argparse

def remover(l, v):
        cl = list(l)
        cl.remove(v)
        return cl

def appender(l, v):
        cl = list(l)
        cl.append(v)
        return cl

def permutation(rest, selected):
        if not rest:
                return ' '.join([str(i) for i in selected])
        else:
                call = [permutation(remover(rest, x), appender(selected, x)) for x in rest]
                return call

def main():
        # Setup parser
        parser = argparse.ArgumentParser(description="Count DNA Nucleotides")
        parser.add_argument("input", metavar='N', type=int, help="A positive integer")
        parser.add_argument("-o", "--output_file", help="Output file containing the result", action="store_true", required=False)
        args = parser.parse_args()

        # args = 4
        perm = permutation(range(1, args.input+1), [])

        if args.output_file:
                with open("results.txt", 'w') as output:
                        output.write('\n'.join([str(i) for i in perm]))
        else:
                print('\n'.join([str(i) for i in perm]))

if __name__ == "__main__":
        main()