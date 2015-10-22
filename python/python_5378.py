# Python - Import file into multiple arrays, dicts, tuples
orar = []
for line in csv.reader(f, delimiter='\t', lineterminator='\t\t', doublequote=False, skipinitialspace=True):
    orar.append(OraRend._make(line[1:]))
