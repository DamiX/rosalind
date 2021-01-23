# Finding a Motif in DNA

## Source
[Rosalind - Finding a Motif in DNA](http://rosalind.info/problems/subs/)

## Problem
Given two strings _s_ and _t_, _t_ is a *substring* of _s_ if _t_ is contained as contiguous collection of symbols in _s_ (as a result, _t_ must be no longer than _s_).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of  all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, ans 18). The symbol at position _i_ of _s_ is denoted by _s[i]_.

A substring of _s_ can be represented as _s[j:k]_, where _j_ and _k_ represent the starting and ending positions of the substring in _s_; for example, if _s_ = "AUGCUUCAGAAAGGUCUUACG", then _s[2:5]_ = "UGCU".

The location of a substring _s[j:k]_ is its beginning position _j_; note that _t_ will have multiple locations in _s_ if it occurs more than once as a substring of _s_ (see the Sample below).

**Given:** Two DNA strings _s_ and _t_ (each of length at most 1 kbp).

**Return:** All locations of _t_ as a substring of _s_.

## Example
Input : s = GATATATGCATATACTT, t = ATAT

Output : 2 4 10

## Usage
```
$ python main.py input_file.txt [-o]
```

## License
[GNU General Public License v3.0](http://www.gnu.org/licenses/)