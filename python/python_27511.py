# Reference undefined to functions in python-dev header
gcc -std=c99 -o main -I /usr/local/include/python3.4m main.c \
  -L /usr/local/lib -lpython3.4m
