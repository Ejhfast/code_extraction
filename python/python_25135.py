# Importing VISA waveform from an oscilloscope into Python
tdsData = inst.query_binary_values('CURVe?', datatype='b', is_big_endian=True)
