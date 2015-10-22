# sys.stdout.write not working properly for binary files on windows
msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
