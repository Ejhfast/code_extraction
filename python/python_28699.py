# Getting command line output of batch file to write to another file
import commands
result = commands.getoutput('ls')
print(result)
