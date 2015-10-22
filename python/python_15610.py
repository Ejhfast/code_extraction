# R system call returning stdin without escape characters
cat(paste(system("./f.py", intern=TRUE), collapse=""))
