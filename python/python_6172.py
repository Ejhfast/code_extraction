# Python imports for tests using nose - what is best practice for imports of modules above current package
import sys, os
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path
