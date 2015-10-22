# Python Read Large Text Files Probelm
with open(in_file1,"r") as f1, open(in_file2,"r") as f2:
    for (line1, line2) in izip(f1, f2):
        compare(line1, line2)
