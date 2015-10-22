# importing NumPy in Parallel Python
job = job_server.submit(aa.plotwavefunc, depfuncs = (band,k), modules = ("numpy","pylab","signal"))
