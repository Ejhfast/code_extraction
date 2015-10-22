# How do I convert Perl's pack 'Nc*' format to struct.pack for Python?
struct.pack('&gt;I', some_integer) + struct.pack('b'*len(long_array), *long_array)
