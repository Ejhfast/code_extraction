# hg verify doesn't return 0 or 1
p = Popen(['hg', 'verify', '-R', 'natrium-master', '-q'], stdout=PIPE, stdin=PIPE)
out, err = p.communicate()
print p.returncode
