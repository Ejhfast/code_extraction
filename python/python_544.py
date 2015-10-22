# How can I detect if a file is binary (non-text) in python?
import mimetypes
...
mime = mimetypes.guess_type(file)
