# String to datetime
from datetime import datetime
datetime.strptime('2010-10-08 14:26:01.220000'[:-7],
                '%Y-%m-%d %H:%M:%S').strftime('%b %d %Y')
