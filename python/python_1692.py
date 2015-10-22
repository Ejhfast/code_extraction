# Implementing preg_match_all in Python
&gt;&gt;&gt; [(m.group(0), m.start()) for m in re.finditer('[aeiou]',s)]
[('u', 1), ('e', 3), ('a', 6), ('i', 8), ('a', 11), ('i', 13), ('i', 15), ('i', 18), ('e', 20), ('i', 23), ('a', 24), ('i', 26), ('o', 28), ('i', 30), ('o', 31), ('u', 32)]
