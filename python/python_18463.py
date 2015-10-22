# Parsing a plaintext document into a python array
text = open('txt_filename').read()
data = eval('[' + text + ']')
