# sorting a list of class instances by attribut ip
key=lambda my_instace: long(''.join(["%02X" % long(i) for i in my_instance.ip.split('.')]), 16))
