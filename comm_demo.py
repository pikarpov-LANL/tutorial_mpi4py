# Here we expand on the plot_demo.py, by introducing
# proper communication via:
#       - bcast
#       - scatter
#       - gather
# which allows our program to switch between serial and
# parallel execution.

# unlike in plot_demo, here we need to:
#       1) do initial data preparation in serial
#          on the master rank
#       2) distribute the assignment to all ranks
#       3) produce our plots in parallel
#       4) gather a metric for each dataset from
#          every rank back on the master rank

# -pikarpov

from mpi4py import MPI
import numpy as np
import time
import matplotlib.pyplot as plt

# set global communication
comm = MPI.COMM_WORLD

# rank is an integer id from 0 to n, 
# unique to every thread
rank = comm.Get_rank()

# size is the number of cores available, i.e. "-n %d"
size = comm.Get_size()

if rank == 0:
    print(f'--- Serial on rank {rank} ---')
    # read in the header and do some fancy data-prep
    # let's say that from the header, we read-in the number of files    
    numfiles = 8
    print(f"Number of files: {numfiles}")
    
    # we will prepare the interval indexes for erach rank to execute
    interval_size = int(numfiles/size)
    print(f"Interval size:   {interval_size}")
    
    interval = np.array([[i*interval_size,i*interval_size+interval_size] for i in range(size)])
    print(f"Intervals: \n{interval}")
    
    print(f'\n-------- Assignments --------')    
else:
    # initialize the variables to be recieved from master rank
    numfiles = 0
    interval = 0

# we want to distribute the header read-in `numfiles` parameter to all
# 'bcast' send the same value to all the ranks
numfiles = comm.bcast(numfiles, root=0)
print(f'rank {rank} received numfiles {numfiles}')

# to synchonize execution, use 'Barrier'
comm.Barrier()
time.sleep(0.01) # this is just to synch the printout

# now let's distribute individual intervals to all
interval = comm.scatter(interval, root=0)
print(f'rank {rank} received interval {interval}')

# synchonizing again
comm.Barrier()
time.sleep(0.1)

dataset_metric = np.zeros(numfiles)

# so this 'for' loop is running in parallel
if rank==0: print("\n--- Parallel for-loop ---", flush=True)
for i in range(interval[0], interval[1]):
    
    # load your data: 1e6 datapoints in this case
    x = np.linspace(0,2*np.pi,int(1e6))   
    y = np.sin(x)
    
    # plot it
    plt.plot(x,y)
    
    plt.savefig(f'rank{rank}_i{i}.png')
    
    # free-up memory by closing the plot;
    # don't forget to unload your datasets too!
    plt.close()
    
    dataset_metric[i] = i
    
    print(f'rank {rank}: finished dataset {i}')
    
print(f'--> rank {rank} is Done!')

# lastly we want to gather some computed data back 
# onto the master rank to produce a plot covering 
# all the dataset

# use 'gather' to concatenate data from all ranks
# on the master rank

dataset_metric = comm.gather(dataset_metric, root=0)

if rank==0:
    print(f'\n--- Back to Serial ---')
    dataset_metric = np.array(dataset_metric)    
    
    print(f'rank {rank} gathered some fancy analysis data:')
    print(dataset_metric)
    
    dataset_metric = sum(dataset_metric)
    
    print('\nFinal version of metrics gathered')
    print(dataset_metric)