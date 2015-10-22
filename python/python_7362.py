# Efficient string to hex function
def StringToHexString(s):
    return ''.join( map(lambda param:hexLoookup[param], map(ord,s) ) )
