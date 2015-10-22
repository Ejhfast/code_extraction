# When trying to build a Python executable with Pyinstaller, fails to find an existing scipy module
def fix_dependencies():
    from scipy.sparse.csgraph import _validation
