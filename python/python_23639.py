# How do I execute a bash function defined in .profile using python subprocess module?
import subprocess
subprocess.call(['bash', '-c', '. ~/.profile &amp;&amp; knife-LHR'])
