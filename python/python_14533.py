# Import module dynamic from a folder python
var = "module"
module = __import__("modules.{0}".format(var), globals(), locals(), [], -1)
