# ZMQ pair (for signaling) is blocking because of bad connection
self.socket = self.context.socket(zmq.DEALER)
    self.socket.setsockopt(zmq.SNDHWM, 200000)
