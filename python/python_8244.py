# Python and py2exe - Implicitely Importing Modules
includes = ['Panels.%s' % os.path.basename(os.path.splitext(filename)[0]) for
        filename in glob.glob('Panels//*.py')]
