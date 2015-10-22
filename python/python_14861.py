# Doing a static type checking at method level, python
def testStatic(self, request):
    assert isinstance(request, TestRequest)
    ...
