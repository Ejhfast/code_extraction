# python zipfile, how do I know an item is a directory?
is_dir = lambda zipinfo: zipinfo.filename.endswith('/')
