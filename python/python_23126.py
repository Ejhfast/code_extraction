# Python App Engine debug/dev mode
IS_DEV_APPSERVER = 'development' in os.environ.get('SERVER_SOFTWARE', '').lower()
