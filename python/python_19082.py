# Python OS command
import subprocess
subprocess.call("service postgresql start ; wait ; service metasploit start ; wait ; armitagedate", shell=True)
