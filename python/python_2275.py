# Python multiprocessing doesn't play nicely with uuid.uuid4()
import os, uuid
return uuid.UUID(bytes=os.urandom(16), version=4)
