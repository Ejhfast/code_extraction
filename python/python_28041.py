# how to send extra arguments to another function
def foo(self, request, method='post', page=None, **options):
    #do something
    self.another_foo(**options)
