# Google Calendar API - 404 on calendar (service account)
credentials = SignedJwtAssertionCredentials(SERVICE_ACCOUNT_EMAIL, key,
      scope='https://www.googleapis.com/auth/calendar', sub=user_email)
