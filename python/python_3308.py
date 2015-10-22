# Flask/Werkzeug how to attach HTTP content-length header to file download
from flask import Response
response = Response()
response.headers.add('content-length', str(os.path.getsize(FILE_LOCATION)))
