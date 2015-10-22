# Expanding/substituting variables in a popen call
p = sp.Popen("echo Hello $FOO", env={"FOO":"42"}, shell=True)
