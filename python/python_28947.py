# How to use mpi4py in IPython notebook?
%%px
from mpi4py import MPI
print MPI.COMM_WORLD.size
