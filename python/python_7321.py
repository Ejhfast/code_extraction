# How to test that a Python function takes less than a certain time to complete
@timed(2.1)
def test():
    func_with_timeout(timeout=2)
