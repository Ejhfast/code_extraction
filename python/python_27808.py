# Windows to Linux script issues: "IndexError: list index out of range"
for x in glob.glob("*raw_vcf.csv"):
   csv_f = open(x, "r")
