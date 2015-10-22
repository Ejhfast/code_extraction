# How to disallow pickle serialization in celery
from kombu import serialization
serialization.registry._decoders.pop("application/x-python-serialize")
