# Python converting UUID's from string
outputFile.write(""" WHERE tableID = '""" + uuid.UUID(parts[-1]) + """'""")
