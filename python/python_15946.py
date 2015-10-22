# To use an existing file for an external operation using Django
open(os.path.join(settings.MEDIA_ROOT, '/media/file.txt'), 'r').read()
