# ctypes initializing c_int array by reading file
f = open('hr.dat', 'rb')
array = (c_int * 32487834)()
f.readinto(array)
