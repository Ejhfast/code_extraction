# how to "conditionally compile" python
portfd = os.open(portname, os.O_RDWR | getattr(os, 'O_NONBLOCK', 0))
