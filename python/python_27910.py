# Strange characters in Django shell, arrowkeys not working
if not os.environ.get("DISABLE_UTF8_REDEFINE"):
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf8')(sys.stderr)
