# How to read/extract lines with more than 20 spaces ? - unix/python
grep -E '(\s[^\s]*){20,}' in.txt | sed 's/^\s*//;s/\s*$//'
