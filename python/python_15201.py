# GAE: remote_api_shell.py uses wrong Django version
from google.appengine.dist import use_library
use_library('django', '1.3')
