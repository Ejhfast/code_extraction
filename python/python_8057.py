# How to turn console echo back on after tty.setcbreak()
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
