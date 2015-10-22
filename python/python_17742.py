# Join strings skips first line
with open(keywords_file, 'r') as f:
     keywords = ",".join(line.strip() for line in f)
