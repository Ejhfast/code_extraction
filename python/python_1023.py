# How to tell when nosetest is running programmatically
if 'nose' in sys.modules:
    print "Nose is running, or at least has been imported!"
    #or whatever you need to do if nose is running
