# Python replace up to \n in a function
def warpbar(text, lineLength):
   n = len(text)
   return "#"*lineLength+"\n"+"="*(n-lineLength)
