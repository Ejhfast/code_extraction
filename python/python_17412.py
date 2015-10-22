# In pyfirmata, how to set up a handler for string messages?
def _messageHandler(self, *args, **kwargs):
    print util.two_byte_iter_to_str(args)
