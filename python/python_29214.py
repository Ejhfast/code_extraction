# Running a system command through python not producing the same output
file_name.flush()
file_name.close()
subprocess.call(['sudo mail -s "Subject" person@example.com &lt; /path/to/file.txt'], shell=True)
