# How to create Library project
import clr
files = [ 'file1.py', 'file2.py' ]    # Look into os.walk() if you have more than a few files
clr.CompileModules('Foo.dll', *files)
