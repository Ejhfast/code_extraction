# Capture output via subprocess w/o using communicate
output = subprocess.check_output('gams "indus89.gms"\r\n', shell=True)
