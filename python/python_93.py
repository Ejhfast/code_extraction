# Translate SVN path to local file system path in Python
baselen = len(self.basePath)
return (path[baselen:].replace("/", "\\") for path in paths)
