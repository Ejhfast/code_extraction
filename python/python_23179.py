# Python: Write Logfile
def writeFile(self,text):
    with open(self.__FullFileName) as fd:
        fd.write(text)
