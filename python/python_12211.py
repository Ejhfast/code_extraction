# How to append/concat a number in re.sub
re.sub(r'(.*_)\d*(\..*)', r'\g&lt;1&gt;8000\2', baseName)
