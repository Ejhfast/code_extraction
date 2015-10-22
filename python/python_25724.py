# Python convert datetime string to date
import dateutil.parser
dateutil.parser.parse('2015-01-28 03:00:00').date()
&gt;&gt;datetime.date(2015, 1, 28)
