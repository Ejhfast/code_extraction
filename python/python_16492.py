# How to remove or replace substring in Python determined by start and end point?
def replace_between(text, begin, end, alternative=''):
    middle = text.split(begin, 1)[1].split(end, 1)[0]
    return text.replace(middle, alternative)
