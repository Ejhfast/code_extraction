# Python - using subprocess to call sed?
out_file = open(outp, "w")
sub = subprocess.call(['sed', 's/\"//g', inp], stdout=out_file )
