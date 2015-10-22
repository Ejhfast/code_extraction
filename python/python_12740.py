# Problems extending twisted.web's static.File class
class TransCodingFile(static.File):
    def render(self,request):
        return static.File.render(self,request)
