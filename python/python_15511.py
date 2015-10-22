# Python bottle module causes "Error: 413 Request Entity Too Large"
import bottle
bottle.BaseRequest.MEMFILE_MAX = 1024 * 1024 # (or whatever you want)
