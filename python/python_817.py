# How to parse a RFC 2822 date/time into a Python datetime?
from email.utils import parsedate_tz
print parsedate_tz('Fri, 15 May 2009 17:58:28 +0700')
