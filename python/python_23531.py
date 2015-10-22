# Including xlrd/xlwt/xlutils with modules outside of python installation
imp.load_source("xlrd",os.path.join(path,"xlrd","__init__.py"))
