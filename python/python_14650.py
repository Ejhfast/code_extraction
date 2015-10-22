# Guaranteed unicode or ascii backoff in Python 2.7
def to_unicode_with_ascii_backoff(text):
    u = UnicodeDammit(text).unicode_markup
    return u if u or not text else text.decode('ascii', 'replace')
