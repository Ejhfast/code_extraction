# encode Netbios name python
encoded_name = ''.join([chr((ord(c)&gt;&gt;4) + ord('A'))
                        + chr((ord(c)&amp;0xF) + ord('A')) for c in original_name])
