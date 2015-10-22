# Python raw_input following sys.stdin.read() throws EOFError
message = sys.stdin.read()
sys.stdin = open('/dev/tty')
selected_index = raw_input('Which URL to open?')
