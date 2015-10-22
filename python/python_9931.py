# How to redirecting "stdout" to a Label widget?
class StdoutRedirector(IORedirector):
        def write(self,str):
           self.TEXT_INFO.config(text=self.TEXT_INFO.cget('text') + str)
