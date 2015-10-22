# displaying newlines in the help message when using python's optparse
class MyParser(optparse.OptionParser):
    def format_epilog(self, formatter):
        return self.epilog
