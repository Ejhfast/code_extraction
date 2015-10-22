# converting a list of times to total time
s = sum(hours)*3600+sum(minutes)*60+sum(seconds)
return '%d hours %d minutes %d seconds'%( s/3600, (s%3600)/60, s%60)
