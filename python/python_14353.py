# A Simple Message Decoder
&gt;&gt;&gt; message = 'HelloWorld'
&gt;&gt;&gt; encoded = ''.join(chr(ord(letter) - 3) for letter in message)
&gt;&gt;&gt; decoded = ''.join(chr(ord(letter) + 3) for letter in encoded)
