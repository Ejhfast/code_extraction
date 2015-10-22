# Can fabric tasks have names that are not valid Python function names?
@task(alias = 'database-reset')
def database_reset():
    ...
