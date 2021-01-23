#!/usr/bin/python
#encoding: utf-8
"""Algorithm module for rosalind"""

def substring(s, motif):
        """
        Return locations of all substring (naive algo)
        For a faster implementation, check my grep implementation here : https://github.com/DamiX/Algo_texte_2016

        Keyword Arguments:
        :param s -- string
        :param motif -- motif
        """
        res = []
        pos = 0
        while True:
                pos = s.find(motif, pos)
                if pos == -1:
                        break
                pos += 1
                res.append(pos)
        return res

def hamming_distance(first, second):
        """
        Compute hamming distance

        Keyword Arguments:
        :param first -- first string
        :param second -- second string
        """
        if len(first) != len(second):
                raise ValueError("Hamming distance cannot be computed from strings of different length")
        return sum(c1 != c2 for c1, c2 in zip(first, second))