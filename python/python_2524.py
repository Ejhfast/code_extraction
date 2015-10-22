# Comments on this assumption about running on dev server vs a real instance in app engine (python)?
DEBUG = os.environ['SERVER_SOFTWARE'].startswith("Dev")
