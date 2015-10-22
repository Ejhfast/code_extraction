# Python3 GZip Compressing String
data = bytes(json.dumps(packet), 'utf-8')
s_out = gzip.compress(data)
