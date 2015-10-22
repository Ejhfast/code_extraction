# Celery is refusing to deserialize content of my custom serialization throwing ContentDisallowed Exception
from kombu.serialization import registry
registry.enable('pickle')
