# logging module for python reports incorrect timezone under cygwin
if os.getenv("TZ"):
    os.unsetenv("TZ")
