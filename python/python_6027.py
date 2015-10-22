# how to fill the paremeter into function name string for invoking?
str1 = 'foo1({0}).foo2({1})'
para = [1,2]
eval(str1.format(*para)) # equivalent to eval(str1.format(1,2))
