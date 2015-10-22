# how to make each key-value of a dictionary print on a new line?
print("{" + "\n".join("{}: {}".format(k, v) for k, v in d.items()) + "}")
