# python subprocess.Popen vs os.popen
cmd = "hadoop fs -ls /projectpath/ | grep ^d | grep -v done | head -1 | awk {'print $8'}"
p = sub.Popen(cmd,stdout=sub.PIPE,stderr=sub.PIPE, shell=True)
