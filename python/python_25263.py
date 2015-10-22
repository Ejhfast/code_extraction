# How to use QProcess in headless script?
p.start("./mainapp.exe", [])
p.waitForFinished()
out = p.readAllStandardOutput()
