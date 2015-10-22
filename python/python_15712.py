# How to clone pexpect winsize from current terminal?
rows, cols = map(int, os.popen('stty size', 'r').read().split())
child.setwinsize(rows, cols)
