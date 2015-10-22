# How do I stop setup.py from trying to include -arch ppc on MacOSX builds?
$ sudo ln -s /Developer/Platforms/iPhoneOS.platform/Developer/usr/libexec/gcc/darwin/ppc /Developer/usr/libexec/gcc/darwin
$ sudo ln -s /Developer/Platforms/iPhoneOS.platform/Developer/usr/libexec/gcc/darwin/ppc /usr/libexec/gcc/darwin
