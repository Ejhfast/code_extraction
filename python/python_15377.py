# python 3 fdfgen unicode TypeError
safe = utf16.replace(b'\x00)', b'\x00\\)').replace(b'\x00(', b'\x00\\(')
return (b'%s%s' % (codecs.BOM_UTF16_BE, safe))
