# Read a file, skip unwanted lines & add into a List
mainlist = [line.strip() for line in f if "New changes" not in line]
