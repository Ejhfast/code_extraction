# Pass empty/noop function/lambda as default argument
def execute(func=None, *args, **kwargs):
    if func:
        func(*args, **kwargs)
