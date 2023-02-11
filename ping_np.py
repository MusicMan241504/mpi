from mpi4py import MPI
import time
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


#Calculate ping time for each node

n = 1000000
if rank == 0:
    data = np.arange(n,dtype='i')
    for i in range(1,size):
        start = time.time_ns()
        for j in range(1000):
            comm.Send(data,dest=i)
            comm.Recv(data,source=i)
        end = time.time_ns()
        time_ns = (end-start)/1000
        print("Rank " + str(i) + ": " + str(round((time_ns)/1000,3)) + " μs")
    comm.Abort()


else:
    data = np.empty(n,dtype='i')
    while True:
        comm.Recv(data,source=0)
        comm.Send(data,dest=0)
