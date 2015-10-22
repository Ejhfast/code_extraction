# Using python-oauth2 I get oauth_parameters_absent:scope
scope = "http://www.google.com/calendar/feeds/default/allcalendars/full"
REQUEST_TOKEN_URL = 'https://www.google.com/accounts/OAuthGetRequestToken?scope={0}'.format(scope)
