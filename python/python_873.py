# app-engine-patch with pyamf = No module named encoding
from google.appengine.dist import use_library
use_library('django', '1.0')
