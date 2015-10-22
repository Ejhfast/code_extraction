# Boto (Python)- reversed bucket list
objs = [obj for obj in self.bucket.list(PREFIX)]
objs.reverse()
