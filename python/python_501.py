# Setting the encoding for sax parser in Python
def test(filename):
    parser = xml.sax.make_parser()
    parser.parse(open(filename))
