# Can you please tell me how can I convert this date string to total seconds in python?
import time
answer = time.mktime(time.strptime(string, '%Y-%m-%d %H:%M:%S'))
