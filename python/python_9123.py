# platform specific Unicode semantics in Python 2.7
def code_points(text):
    utf32 = text.encode('UTF-32LE')
    return struct.unpack('&lt;{}I'.format(len(utf32) // 4), utf32)
