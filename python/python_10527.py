# Python multiprocessing Queue failure
from multiprocessing import Manager
manager = Manager()
result_queue = manager.Queue()
