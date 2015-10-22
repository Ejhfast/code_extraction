# Python SocketServer - Get own IP
import urllib.request
external_ip = urllib.request.urlopen('http://ifconfig.me/ip').read()
