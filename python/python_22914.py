# ssh for df -h using python to display selected information only
sub_process=subprocess.Popen(["ssh", "hostname", "df -h"], stdout=subprocess.PIPE)
stdout_file=sub_process.stdout
first_line=stdout_file.readline()
