# Get the string between first two \ and \
In [8]: a = ['\\Mango\\stone\\forest\\', '\\Orange\\sand\\house\\', '\\Rabbit\\cage\\village\\']
In [11]: [x.split('\\')[1] for x in a]
Out[11]: ['Mango', 'Orange', 'Rabbit']
