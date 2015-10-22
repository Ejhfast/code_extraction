# Python, handling session in CGI
if not 'seen' in session.data:
    # new session, set a flag
    session.data['seen'] = True
