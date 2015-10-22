# Run a Java main class using its relative path? (Python)
output = subprocess.check_output("java MyJavaClass", cwd="../../bin/")
