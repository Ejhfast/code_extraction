# Regular expression: replace the suffix of a string ending in '.js' but not 'min.js'
outfile = re.sub(r"(?&lt;!\.min)\.js$", ".min.js", infile)
