# Python-Requests (>= 1.*): How to disable keep-alive?
s = requests.session()
s.keep_alive = False
