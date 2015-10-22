# set LOG_ENABLED=FALSE on scrapy
from scrapy.conf import settings
settings.set('LOG_ENABLED', False ,priority='cmdline')
