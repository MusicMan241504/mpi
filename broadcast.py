from mpi4py import MPI
import random as rand
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = [rand.randint(1,100) for i in range(100)]
else:
    data = None
data = comm.bcast(data, root=0)
print(data)

