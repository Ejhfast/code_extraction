# Python3 - Creating a scanner for a compiler and getting errors upon testing
while token != None:
 print(scanner.consume(token))
 token = scanner.lookahead()
