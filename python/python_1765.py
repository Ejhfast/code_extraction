# A list vs. tuple situation in Python
d = {(1, 2): 'a', (3, 8, 1): 'b'}  # Valid.
d = {[1, 2]: 'a', [3, 8, 1]: 'b'}  # Error.
