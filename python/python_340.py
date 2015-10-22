# Validating Oracle dates in Python
import dateutil.parser
d= dateutil.parser.parse('1/2/2003')
d.strftime('%d-%b-%y')
