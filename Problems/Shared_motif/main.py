import os
import argparse

def generate_substring(input, substr_length):
        """
        Generate substring from input of the given length

        :param input -- input string
        :param substr_length -- length of the substring
        """
        res = []
        for i in range(len(input)-substr_length+1):
                sub = input[i:i+substr_length]
                if sub not in res:
                        res.append(sub)
        return res

def contain_motif(data_collection, motif):
        for s in data_collection:
                if s.find(motif) == -1:
                        return False
        return True

def find_shared_motif(data_collection):
        """
        Find the longest common substring

        :param data_collection -- array of strings
        """
        substring = min(data_collection)
        data_collection.remove(substring)

        i = len(substring)
        while i > 0:
                subs = generate_substring(substring, i)
                for sub in subs:
                        if contain_motif(data_collection, sub):
                                return sub
                i -= 1
        return ""

def read_fasta(content):
        """
        Read fasta content
        """
        res = dict()
        value = ""
        for s in content:
                s = s.strip()
                if s[0] == '>':
                        if value:
                                res[key] = value
                                value=""
                        key = s[1::]
                else:
                        value += s
        res[key] = value
        return res

def main():
        # Setup parser
        parser = argparse.ArgumentParser(description="Count DNA Nucleotides")
        parser.add_argument("input_file", help="Input file containing k-mers input")
        parser.add_argument("-o", "--output_file", help="Output file containing the result", action="store_true", required=False)

        args = parser.parse_args()

        with open(args.input_file, 'r') as f:
                content = f.readlines()

        data = read_fasta(content)
        dna_collection = data.values()

        res = find_shared_motif(dna_collection)

        if args.output_file:
                with open("results.txt", 'w') as output:
                        for idx, value in data.items():
                                output.write(idx + '\n')
                                output.write(value + '\n')
        else:
                print(res)

if __name__ == "__main__":
        main()