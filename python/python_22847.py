# Error when running ant script using python subprocess
subprocess.call(['ant','-f','lib/java/build.xml','-Dno-gen-thrift=\"\"','-Dtestargs', '\"--protocol=binary', '--transport=buffered\"','run-testserver'])
