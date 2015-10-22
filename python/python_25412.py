# Does the Gmail API support using OAuth Service Accounts?
credentials = SignedJwtAssertionCredentials(client_email, private_key,
  'https://www.googleapis.com/auth/gmail.readonly', sub='user@domain.com')
