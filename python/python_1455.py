# change desktop background
import commands
command = "gconftool-2 --set /desktop/gnome/background/picture_filename --type string '/path/to/file.jpg'"
status, output = commands.getstatusoutput(command)  # status=0 if success
