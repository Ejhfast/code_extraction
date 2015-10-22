# Clear buffered input stream
def write(self, text):
    if text!="\n":
       self.stdout.write('###' + text)
