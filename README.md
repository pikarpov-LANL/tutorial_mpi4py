# Tutorial on `mpi4py`

This is a quick-start guide to mpi4py to run simple scripts, e.g. for making plots in parallel. Setup instructions along with some example scripts are provided in this repo.

# Setup

## Anaconda
To simplifying installation and to setup our workspace, let's install Anaconda. You can downloaad it straight from the official website of [Anaconda](https://www.anaconda.com/products/distribution). 

For example, on Linux, you can download the version from `05.2022` by running below.

```
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
```

To install it, run:
```bash
bash https://www.anaconda.com/products/distribution
```
Go through the install process, and make sure to initialize `conda`. Afterwards, to activate `conda`, run:
```bash
source ~/.bashrc
```

Lastly, create a new virtual environment to mess around:
```bash
conda create -n py310 python=3.10
```
The above create an environment named `py310` with a python version 3.10. The last thiing you need to do is to activate it.
```bash
conda activate py310
```
To the right of your login name you should see the name of the environment you are in as such: `(py310)login@host`


## Python
Make sure you are running python 3.5+ (3.10+ recommended) for this tutorial. That said, `mpi4py` should work on python 2.7 just fine.

## OpenMPI & mpi4py

Install openmpi & mpi4py via `conda`
```bash
conda install -c conda-forge mpi4py openmpi
```
If you don't want to use `conda`, or would like to use MPICH/Microsoft MPI, follow [mpi4py's Documentation](https://pypi.org/project/mpi4py/).


# Running Examples


## Check the CPUs
To run an example in parallel, first you should check how many threads are available on your machine. You can do that via 
```bash
lscpu
```
Look at the 5th line form the top labeled 'CPU(s):'

Altenatively you can check the number of threads with
```bash
htop
```

```diff
! Note: cores and threads are different, with modern machines typically having 2 threads per core.
```

## Run

To run in paralle, you need to specify how many thread to give to the process. Below, the cript will be run with 4 threads.
```bash
mpirun -n 4 python demo.py
```
