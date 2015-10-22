# Always an Error on the First Message
return "HTTP/1.1 101 WebSocket Protocol Handshake\r\nUpgrade: WebSocket\r\nConnection: Upgrade\r\nSec-WebSocket-Origin: %s\r\nSec-WebSocket-Location: ws://%s%s\r\nSec-WebSocket-Protocol: sample\r\n\r\n%s"% (origin, host, resource, token)
