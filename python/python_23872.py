# python - ctypes error with mysql c
gcc -c -fPIC lib1.c
gcc -shared lib1.o -o lib1.so $(mysql_config --libs) $(mysql_config --cflags)
