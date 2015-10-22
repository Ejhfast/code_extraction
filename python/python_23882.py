# Reformatting text file
sed 's/\(.\{128\}.\{22\}[^ ]*\) /\1\
/g' YourFile
