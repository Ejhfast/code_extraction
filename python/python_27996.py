# How do I get python to fetch information from command prompt such as 'tasklist'
from subprocess import check_output
var = check_output('tasklist')
