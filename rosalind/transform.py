#!/usr/bin/python
#encoding: utf-8
"""Transformation module"""

import defs

def DNA_to_RNA(dna):
        """
        Return a RNA string for a DNA string

        Keyword argument:
        :param dna, str -- dna string
        """
        return dna.replace('T', 'U')

def reverse_complement(dna):
        """
        Reverse complement a DNA string

        Keyword argument:
        :param dna, str -- dna string
        """
        complements = {'A':'T','T':'A','C':'G','G':'C'}
        return ''.join(map(lambda x: complements[x], dna[::-1]))

def RNA_to_PROTEIN(rna):
        """
        Convert rna string to protein string

        Keyword argument:
        :param rna, str -- rna string
        """
        sz_rna = len(rna)
        assert(not bool(sz_rna%3)) # Throw exception

        rna = rna.upper()
        output = ''

        for i in range(0, sz_rna, 3):
                conv = defs.rna_codon_table[rna[i:i+3]]
                if conv == "Stop":
                        break
                else:
                        output += conv
        return output
