# Cannot seem to crawl a deep directory with my Python script, any idea?
correctlyNamedDirectories = [os.path.join(path, subname) for path, dirnames, filenames in os.walk(directory) for subname in dirnames + filenames]
