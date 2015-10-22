# How to output a BlobProperty from my model to a hex string
self.response.out.write(''.join([hex(z)[2:].zfill(2) for z in bytearray(puzzleset_instance.img)]))
