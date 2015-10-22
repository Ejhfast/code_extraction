# How do I use Cython for external module compilation, from within my setup.py file?
setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("myext", ["myext.pyx", "myextlib.pyx"])])
