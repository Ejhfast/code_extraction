# Extract substring from list of file names in Python or R
[re.search(r'data_(.+?)_48P', i).group(1) for i in files if re.search(r'data_.+?_48P', i)]
