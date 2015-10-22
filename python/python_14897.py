# Reading Java system.out.print via Python subprocess
p1 = subprocess.Popen(["/usr/bin/java", "MyClass"], stdout=subprocess.PIPE)
print p1.stdout.read()
