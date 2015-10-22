# Remove string between 2 characters from text string
In [11]: re.sub(r'\[.*?\]', '', 'abcd[e]yth[ac]ytwec')
Out[11]: 'abcdythytwec'
