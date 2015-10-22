# Is there easy way to prevent echo from input?
if sys.stdin is not sys.__stdin__:
    return fallback_getpass(prompt, stream)
