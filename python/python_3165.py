# XML parser syntax error
url = '%s%s/?api_key=%s&amp;method=%s&amp;%s'% \
      (HOST, API, API_KEY, method, _get_auth_url_suffix(method, auth, params))
payload = '%s' % (urlencode(params))
