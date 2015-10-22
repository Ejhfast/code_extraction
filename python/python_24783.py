# Google Admin SDK error Resource Not Found: domain when trying to list existing users
credentials = SignedJwtAssertionCredentials(client_email, private_key,
                        OAUTH_SCOPE, sub='admin@domain.com')
