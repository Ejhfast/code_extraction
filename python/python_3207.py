# python print not functioning correctly after using curses
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
