# ply lexmatch regular expression has different groups than a usual re
c = re.compile("(?P&lt;%s&gt;%s)" % (fname,f.__doc__), re.VERBOSE | self.reflags)
