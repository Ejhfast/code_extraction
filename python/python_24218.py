# Why is my variable not be included in my subprocess.Popen?
subprocess.Popen(['./script.sh ' + variable] , shell=True, stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
