# Python 2.5 - multi-threaded for loop
from multiprocessing import Pool
pool = Pool(processes=5)
pages = pool.map(visit, get_lines(file))
