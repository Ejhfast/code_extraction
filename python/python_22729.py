# assertRaisesRegexp does work with unicode in Python2
raise Exception(u'\u4e2d\u6587'.encode('utf8'))
