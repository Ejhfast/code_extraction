# How to strip entire HTML, CSS and JS code or tags from HTML page in python
def strip_tags(value):
    """Returns the given HTML with all tags stripped."""
    return re.sub(r'&lt;[^&gt;]*?&gt;', '', force_unicode(value))
