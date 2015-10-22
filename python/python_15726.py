# Python fastest way to remove multiple spaces in a string
front_space = lambda x:x[0]==" "
trailing_space = lambda x:x[-1]==" "
" "*front_space(text)+' '.join(text.split())+" "*trailing_space(text)
