# Python: Create multiple lists with increasing size
import random
 [[random.randint(1, 1000) for _ in range(list_size)] for list_size in range(1,4)]
