# Django objects being "non subscriptable" leads me to write redundant code
for attr, value in info.items():
    setattr(me, attr, value)
