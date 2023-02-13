from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#Calculate ping time for each node


if rank == 0:
    num = 1
    for i in range(1,size):
        start = time.time_ns()
        for j in range(1000):
            comm.send(num,dest=i)
            comm.recv(source=i)
        end = time.time_ns()
        time_ns = (end-start)/1000
        print("Rank " + str(i) + ": " + str(round((time_ns)/1000,3)) + " μs")
    comm.Abort()


else:
    while True:
        num = comm.recv(source=0)
        comm.send(num,dest=0)

