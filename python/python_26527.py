# How can I write find and exec command in python
import glob,subprocess
for json_file in glob.glob("/home/tmp/*.json"):
    subprocess.Popen(["python","/path/to/my.py",json_file],env=os.environ).communicate()
