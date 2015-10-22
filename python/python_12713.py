# Injecting variable before/during import
__import__('blah', dict(jim=1, **globals()))
