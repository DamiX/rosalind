#!/usr/bin/python
#encoding: utf-8
"""IO module for rosalind"""

def read_fasta(filepath):
        """
        FASTA format is a notation to store genetic strings.
        Every string begining with a '>' symbol is the label of the following
        genetic string.

        Keyword arguments:
        :param filepath, string -- file in FASTA format
        """
        label, genetic_seq = '', ''
        genetic_collection = dict()

        with open(filepath, 'r') as f:
                buffer = f.readline().strip()
                while buffer:
                        if buffer.startwith('>'):
                                if label:
                                        genetic_collection[label] = genetic_seq
                                        genetic_seq = ''
                                label = buffer
                        else:
                                genetic_seq += buffer
                        buffer = f.readline().strip()

        return genetic_collection