from mpi4py import MPI
import time
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


#Calculate ping time for each node


if rank == 0:
    data = np.arange(10000,dtype='i')
    for i in range(1,size):
        start = time.time_ns()
        for j in range(100000):
            comm.Send(data,dest=i)
            comm.Recv(data,source=i)
        end = time.time_ns()
        time_ns = (end-start)/100000
        print("Rank " + str(i) + ": " + str(round((time_ns)/1000,3)) + " μs")


else:
    while True:
        data = np.empty(10000,dtype='i')
        comm.Recv(data,source=0)
        comm.Send(data,dest=0)
