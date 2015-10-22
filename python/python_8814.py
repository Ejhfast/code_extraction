# Python: how to use 'exec' with custom scope?
def foo() : print( foo.bar )
exec "foo.bar = bar\n" + "foo()" in dict( globals(), bar = 1 )
