# Python-Requests close http connection
s = requests.session()
s.config['keep_alive'] = False
