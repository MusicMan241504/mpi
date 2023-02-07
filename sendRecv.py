from mpi4py import MPI
import random as rand
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 1:
    data = [rand.randint(1,100) for n in range(100)]
    comm.send(data,dest=0)
if rank == 2:
    data = [rand.randint(1,100) for n in range(100)]
    comm.send(data,dest=0)
if rank == 0:
    data = []
    data.append(comm.recv(source=1))
    data.append(comm.recv(source=2))
    print(data)
