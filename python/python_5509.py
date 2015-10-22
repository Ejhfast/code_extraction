# Python: How to deal with non-subscriptable objects?
for service in accounts:
        for account, creds in accounts[service].iteritems():
            account.setupAccount(creds['username'], creds['password'])
