# removing the question mark in python output
Unicode Decryption
How to find out if element is in any dictionary for specific key in list of dictionaries?
def search(name, listofdict):
    return any( d["name"]==name for d in listofdict )
