# python replace ; with , if line starts with keyword
if line.strip().startswith('keywords'):
    line = line.replace(';',',')
outfile.write(line)
