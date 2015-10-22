# Python: test regular expression for end of a sequence of results
def is_end( s ) :
    end_re = re.compile(r'([\d]*,?[\d]*) of \1 results')
    return bool(end_re.search(s))
