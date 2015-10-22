# Retrieving information stored in other sessions with gae-sessions
for activesession in SessionModel.all():
    data = Session._Session__decode_data(activesession.pdump)
    logged_in.append(data['user'])
