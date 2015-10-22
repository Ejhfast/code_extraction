# Counting fully rendered requests
HttpResponse.__bases__ += (FullLoggingHttpResponse,)
