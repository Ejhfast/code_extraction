# Python Multiprocessing Worker/Queue
pool = Pool(processes=6) # run no more than 6 at a time
pool.map(run_assignments_parallel, project_list) # pass full list (12 items)
