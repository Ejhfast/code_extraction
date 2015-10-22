# Import module from specific folder
import imp
yourModule = imp.load_source('yourModuleName', '/path/to/yourModule.py')
foo = yourModule.YourFunction("You", "get", "the", "idea.")
