#!/usr/bin/python
# encoding: utf-8

rna_codon_table = {
        "UUU": "F", "UUC": "F",
        "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
        "UAU": "Y", "UAC": "Y",
        "UGU": "C", "UGC": "C",
        "UGG": "W",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H",
        "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I",
        "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N",
        "AAA": "K", "AAG": "K",
        "GUU": "V", "GUG": "V", "GUA": "V", "GUG": "V", "GUC": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
        "UAA": "Stop", "UAG": "Stop", "UGA": "Stop"
}