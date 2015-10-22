# return dynamic generated file without creating tmp version?
cmd = ['convert', local_file, '-crop', '50%x50%+10+10', '-']
new_image = subprocess.check_output( cmd )
response = HttpResponse( new_image, mimetype=mt )
