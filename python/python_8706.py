# Python Replace an Undetermined length of Text
pattern = "_([^_]*)_"
re.sub(pattern, r'&lt;b&gt;\1&lt;/b&gt;', text)
