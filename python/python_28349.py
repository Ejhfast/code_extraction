# VirusTotal error: UnicodeDecodeError: 'ascii' codec can't decode byte 0xff in position 0: ordinal not in range(128)
import sys
reload(sys)
sys.setdefaultencoding('utf8')
