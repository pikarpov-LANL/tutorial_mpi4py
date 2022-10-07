This is a quick-start guide to `mpi4py` to run simple scripts, e.g. for making plots in parallel. Setup instructions along with some example scripts are provided in this repo. No `sudo` required.

- [Setup](#setup)
    - [Anaconda](#anaconda)
    - [Python](#python)
    - [OpenMPI](#openmpi)
    - [mpi4py](#mpi4py)
- [Running Examples](#running-examples)
    - [Check the CPUs](#check-the-cpus)
    - [Run](#run)

# Setup

### Anaconda
To simplifying installation and to setup our workspace, let's install Anaconda. You can download it straight from the official website of [Anaconda](https://www.anaconda.com/products/distribution). 

For example, on Linux, you can download the version from `05.2022` by running below.

```
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
```

To install it, run:
```bash
bash Anaconda3-2022.05-Linux-x86_64.sh
```
Go through the install process, and make sure to initialize `conda`. Afterwards, to activate `conda`, run:
```bash
source ~/.bashrc
```

Lastly, create a new virtual environment to mess around:
```bash
conda create -n py310 python=3.10
```
The above creates an environment named `py310` with a python version 3.10. The last thing you need to do is to activate it.
```bash
conda activate py310
```
To the right of your login name you should see the name of the environment you are in as such: `(py310)login@host`


### Python
Make sure you are running python 3.5+ (3.9+ recommended) for this tutorial. That said, `mpi4py` should work on python 2.7 just fine.

### OpenMPI

Install OpenMPI & mpi4py via `conda` from channel `conda-forge`. It is a community-led conda repo that has the most up-to-date package versions. The main anaconda channel doesn't even support python 3.9 which is shipped standard with their latest release.
```bash
conda install -c conda-forge openmpi=4.1.4=ha1ae619_100
```
You can also build OpenMPI from source by following their [instructions](https://docs.open-mpi.org/en/v5.0.x/installing-open-mpi/quickstart.html)

> :warning: Note the specific build hash (ha1ae619_100, from July, 2022) when installing openmpi. The 'stable' 4.1.3 & 4.1.4 fail to install essential libraries, making MPI unusable.
### mpi4py

```bash
conda install -c conda-forge mpi4py
```

If you don't want to use `conda`, or would like to use MPICH/Microsoft MPI, follow [mpi4py's Documentation](https://pypi.org/project/mpi4py/).


# Running Examples

### Check the CPUs
To run an example in parallel, first you should check how many **cores** (<ins>not</ins> threads) are available on your machine. You can do that via 
```bash
lscpu
```
Look at the 12th line form the top labeled `Core(s) per socket:`

> :warning: Note: cores and threads are different; modern CPUs typically have 2 threads per core.

### Run

To run in parallel, you need to specify how many cores to give to the process. Below, the cript will be run on 4 cores.
```bash
mpirun -n 4 python simple_demo.py
```
Below is a table describing each demo provided in this tutorial.

| Demo        | Description                                                              |
| :---------- | :----------------------------------------------------------------------- |
| simple_demo | basic test of correct installation                                       |
| plot_demo   | independent `for` loop parallelization with plotting                     |
| comm_demo   | communication demo presenting `send`, `receive`, `gather`, and `barrier` |

If you want to parallelize a code with only *some* independent loops, use the `comm_demo` for guidence.

