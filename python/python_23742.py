# Python regexp find non-repeated statement in source code
(MyType\s+(\S+)\([^)]+\)\s*;)(?!.*MyType\s+\2\(\s*\)\s*;)
