# Translating RNA into Protein

## Source
[Rosalind - Translating RNA into Protein](http://rosalind.info/problems/prot/)

## Problem
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all leters except for B, J, O, U, X and Z). *Protein strings* are constructed from these 20 symbols. Henceforth, the term *genetic string* will incorporate protein strings along with *DNA strings* and *RNA string*.

The *RNA codon table* dictates the details regarding the encoding of specific codons into the amino acid alphabet.

**Given:** An *RNA string* _s_ corresponding to a strand of mRNA (of lenght at most 10 kbp).

**Return:** The protein string encoded by _s_.

## Example
Input : AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Output : MAMAPRTEINSTRING

## Usage
```
$ python main.py input_file.txt [-o]
```

## License
[GNU General Public License v3.0](http://www.gnu.org/licenses/)