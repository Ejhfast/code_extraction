# Python nose tests (actually the error is from Mox) print out errors one character per line (with line numbers!)
if isinstance(self._expected_methods, basestring):
  self._expected_methods = self._expected_methods.split("\n")
