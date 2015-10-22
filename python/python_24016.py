# How to get the matching element of a set in Python 3?
def canonicalize(state, canonical_states):
    return canonical_states.setdefault(state, state)
