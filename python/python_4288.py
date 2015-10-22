# Statically linking OpenSSL with M2Crypto
-self.libraries = ['ssleay32', 'libeay32']
+self.libraries = ['ssleay32', 'libeay32', 'crypt32', 'user32', 'gdi32', 'kernel32', 'ws2_32', 'advapi32']
