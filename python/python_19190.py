# How to create a non-UTF8 string?
Python Pandas create column based on value of index
lengthDF['size'] = 'large'
lengthDF['size'][lengthDF.index &lt; 10] = 'small'
