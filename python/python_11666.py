# remove last STDOUT line in Python
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
print(CURSOR_UP_ONE + ERASE_LINE)
