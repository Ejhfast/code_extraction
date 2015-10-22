# How can I remove first line from fasta file?
with open('path','r') as f:
    content = f.readlines()[1:]
output="".join(content)
