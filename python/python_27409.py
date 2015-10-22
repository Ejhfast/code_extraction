# How to serialise Pandas to MessagePack format as a python buffer / memoryview?
buffer = io.BytesIO()
df.to_msgpack(buffer, append=False, compress='zlib')
