# python - how to check whether some given date exists in netcdf file
timesteps   = ncfile.variables['time']
dates_to_skip = set(['June 23th', 'May 28th', 'April 1st'])
filtered_timesteps = filter(lambda t: t not in dates_to_skip, timesteps)
