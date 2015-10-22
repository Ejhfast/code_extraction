# How do I yield results from a nested Python generator function?
def SmallGenerator():
    for item in GeneratorFunction(3):
        yield item
