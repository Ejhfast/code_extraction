# Extending Google Appstats
from google.appengine.ext.appstats import recording
recording.recorder.record_custom_event('hello', 'data')
