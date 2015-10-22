# Converting dot to png in python
from subprocess import check_call
check_call(['dot','-Tpng','InputFile.dot','-o','OutputFile.png'])
