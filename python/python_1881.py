# Calling Java app with "subprocess" from Python and reading the Java app output
p1 = subprocess.Popen(["/usr/bin/java", "MyClass"], stdout=subprocess.PIPE)
print p1.stdout.read()
