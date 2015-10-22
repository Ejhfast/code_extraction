# Import specific class or function in Python Parallel job
exec("jobserver.submit(get_os_name,modules=('os',))")
