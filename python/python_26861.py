# Running a "piping" script from an os.system() command
import subprocess
proc = subprocess.Popen( [ '/usr/local/bin/monitor' ], stdout=subprocess.PIPE )
stdout, _ = proc.communicate()
