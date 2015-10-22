# When a socket error occur, how to get its errorcode from the exception?
except EnvironmentError as e:
    print e.errno
