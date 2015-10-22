# Problem with cgi-bin python program putting output in wrong place
stdout, stderr = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr.PIPE).communicate()
