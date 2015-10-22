# How do I translate a ISO 8601 datetime string into a Python datetime object?
import dateutil.parser
yourdate = dateutil.parser.parse(datestring)
