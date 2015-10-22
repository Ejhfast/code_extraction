# FutureSession: socket connections not closed
future = self.session_pages.get(url, timeout=20, headers={'Connection':'close'})
