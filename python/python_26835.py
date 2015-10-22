# Combine single and multi argument variables in a function call for Python
def getProperty(self,x, *key):
    key = (x,)+key
    return {k:self.__properties[k] for k in key if k in self.__properties}
