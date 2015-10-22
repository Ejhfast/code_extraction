# How do I use gdb when I'm using a debug version of Python?
LD_PRELOAD=/usr/lib/libpython2.7.so gdb -ex 'set environ LD_PRELOAD' --args my-program-to-debug
