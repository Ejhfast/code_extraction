# Passing meta-characters to Python as arguments from command line
&gt;&gt;&gt; r'\t\n\v\r'.decode('string-escape')
'\t\n\x0b\r'
