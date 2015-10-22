# Execute if no exception thrown
result = type, self.message_handlers[type](self, length - 1)
self.last_recv_time = time.time()
return result
