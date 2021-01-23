import argparse

def compute_gc_content(dna):
        """
        Compute GC Content for the given dna string

        :param dna -- dna string
        """
        sz_dna = 0
        gc_counter = 0

        for c in dna:
                if c == 'C' or c == 'G':
                        gc_counter += 1
                sz_dna += 1
        return (float(gc_counter)/sz_dna) * 100

if __name__ == "__main__":
        # Setup parser
        parser = argparse.ArgumentParser(description="Computing GC Content")
        parser.add_argument("input_file", help="Input file containing DNA strings in FASTA format")
        parser.add_argument("-o", "--output_file", help="Output file", action="store_true")
        args = parser.parse_args()

        with open(args.input_file, 'r') as f:
                content = [s.strip() for s in f.readlines()]

        dna_db = dict(zip(content[::2], content[1::2]))

        max_gc_content = ('', 0)
        for idx, dna in dna_db.items():
                current_gc_content = compute_gc_content(dna)
                max_gc_content = (idx, current_gc_content) if max_gc_content[1] < current_gc_content else max_gc_content

        if args.output_file:
                with open("result.txt", 'w') as output:
                        output.write(max_gc_content[0][1::])
                        output.write(max_gc_content[1])
        else:
                print(max_gc_content[0][1::])
                print(max_gc_content[1])