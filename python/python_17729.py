# Python: get OS language
import locale
loc = locale.getlocale() # get current locale
locale.getdefaultlocale() # Tries to determine the default locale settings and returns them as a tuple of the form (language code, encoding); e.g, ('en_US', 'UTF-8').
