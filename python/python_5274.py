# Python, pipes, and the "-c" option in the command line
cat file | grep apple | python -c "for line in __import__('sys').stdin: print line.replace(\"apple\", \"orange\"),"
