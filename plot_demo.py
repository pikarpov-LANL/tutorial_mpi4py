# The example shows how to parallelize independent
# 'for' loops. Here we parallelize production of plots.

# -pikarpov

from mpi4py import MPI
import numpy as np
import matplotlib.pyplot as plt

# set global communication
comm = MPI.COMM_WORLD

# rank is an integer id from 0 to n, 
# unique to every thread
rank = comm.Get_rank()

# let's say we need to produce plots from 8 datasets
# using 4 cores, meaning 2 plots per thread

start_pool = np.array([0,2,4,6])

start = start_pool[rank]

# 'start' index is unique for each rank,
# so this 'for' loop is running in parallel
for i in range(start, start+2):
    
    # load your data: 1e6 datapoints in this case
    x = np.linspace(0,2*np.pi,int(1e6))   
    y = np.sin(x)
    
    # plot it
    plt.plot(x,y)
    
    plt.savefig(f'rank{rank}_i{i}.png')
    
    # free-up memory by closing the plot;
    # don't forget to unload your datasets too!
    plt.close()
    
    print(f'rank {rank}: finished dataset {i}')