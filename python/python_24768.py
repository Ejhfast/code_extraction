# How can I handle mal-encoded character with Python 2?
response.read().decode('shift_jis_2004',errors='ignore')
