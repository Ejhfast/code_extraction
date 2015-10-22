# Converting specific time format with strptime
import time
log = '16/Jan/2010:18:11:06 +0100'
dt = time.strptime(log, '%d/%b/%Y:%H:%M:%S +0100')
