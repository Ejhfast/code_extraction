# Python subprocess Messy output
output = subprocess.check_output(['wmic', 'PATH', 'Win32_videocontroller',  'GET', 'description'], universal_newlines=True)
print(output , "\n")
