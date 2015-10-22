# try catch coding pattern in python
except (AttributeError, IndexError, NameError, TypeError) as e:
    print "%s was raised... " % (e.__class__.__name__)
