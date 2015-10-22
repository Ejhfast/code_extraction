# How to modify the default location where the python script is trying to write the log
from os.path import expanduser
homedir = expanduser("~")
parser.add_option("-L", "--logfile", dest="logfile", default=os.path.join(homedir, "log-name.log"), help="log messages to LOGFILE [default: %default]", metavar="LOGFILE")
