# "UnicodeDecodeError : 'ascii' codec can't decode byte" when handling Chinese language command line arguments with ElementTree
a_value = sys.argv[1].decode('GB2312')
b_value = sys.argv[2].decode('GB2312')
