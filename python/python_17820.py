# How to use '>>' in popen subprocess
subprocess.Popen("sha256sum file1.zip", stdout = file("file2.sha", "a"))
