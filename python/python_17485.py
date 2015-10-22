# How to write raw bytes to Google cloud storage with GAE's Python API
gcs_file = gcs.open(filename,'w',content_type='audio/mp3')
gcs_file.write(buf.encode('utf-8'))
gcs_file.close()
