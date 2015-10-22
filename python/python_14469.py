# Inserting variables inside .add_argument version
version = '1.0'
parser.add_argument('--version', action='version', version='%(prog)s {}'.format(version))
