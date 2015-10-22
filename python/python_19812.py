# How to read output from subprocess without printing to terminal?
args = ("path\to\application.exe", "--version")
subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
