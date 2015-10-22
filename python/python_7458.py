# Import parent module package
#import package1.subpackage1 as subpackage1 # AttributeError: 'module' object has no attribute 'subpackage1'
subpackage1 = sys.modules[__name__.rpartition('.')[0]] # parent module
