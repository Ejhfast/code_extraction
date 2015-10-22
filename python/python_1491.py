# Display objects within a function, how to NOT terminate the program after close the display?
import os
if os.fork() == 0: exit()
