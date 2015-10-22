# Can I get the output of "print" statement in pythonw?
import sys
sys.stdout = open("mylog.txt", "w")
