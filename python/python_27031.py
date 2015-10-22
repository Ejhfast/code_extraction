# PYTHON - why multiprocessing Pool using 100% of CPU?
cpu_count = multiprocessing.cpu_count()
Pool(processes=cpu_count // 2) # Use only half of the CPUs
