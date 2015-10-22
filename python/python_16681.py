# Using unittest.mock to patch input() in Python 3
@patch('builtins.input', lambda: 'y')
