# Getting envisage services in a Handler
def __init__(self, application, **traits):
     Handler.__init__(self, **traits)
     self.application = application
