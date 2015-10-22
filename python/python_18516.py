# how to start external system application in python specifying startup directory?
import subprocess
subprocess.check_call( ['ls'], cwd='/tmp' )
