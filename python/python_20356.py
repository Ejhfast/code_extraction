# Python - Regular Expression replace all non alpha-numerics EXCEPT periods/decimal points?
print re.sub(r'[^\w.]+', '', "He&amp;y wha*t i%%s 4.6 plu^s 6.4?")
