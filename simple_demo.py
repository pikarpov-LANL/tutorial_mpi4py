# This is the simplest example of how to use mpi4py
# to print from each thread in parallel
#
# -pikarpov

from mpi4py import MPI

# set global communication
comm = MPI.COMM_WORLD

# rank is an integer id from 0 to n, 
# unique to every thread
rank = comm.Get_rank()

print(f'I am rank {rank}')