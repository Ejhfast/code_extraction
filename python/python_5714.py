# Error "wrong ELF class" using ctypes
gcc -c -fPIC -m64 -std=c99 -lm -D_GNU_SOURCE -Wall -pedantic -fopenmp -o foo.o foo.c
gcc -m64 -shared -Wl,-soname,libfoo.so -o libfoo.so foo.o
