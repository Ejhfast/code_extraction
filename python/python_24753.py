# when convert to base 64, TypeError: 'str' does not support the buffer interface
encodedMsg = base64.b64encode(self.msg.encode('ascii'))
