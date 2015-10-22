# python - need help inserting text files with open() into mysql
with open(filename,"r") as infile:
    cursor.execute("insert into mytable (file_contents) values (%s)", (infile.read(), ))
