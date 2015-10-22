# pyCurl WRITEFUNCTION callback with parameters
connn.setopt(pycurl.WRITEFUNCTION, lambda data: real_impl(data, param1, param2))
