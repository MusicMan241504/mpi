from mpi4py import MPI
import numpy as np

#create communicator
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#create arrays
if rank == 0:
    a = np.random.randint(100,size=100,dtype='i')
    b = np.random.randint(100,size=100,dtype='i')
else:
    a = np.empty(100,dtype='i')
    b = np.empty(100,dtype='i')

#broadcast arrays
comm.Bcast(a,root=0)
comm.Bcast(b,root=0)

#calculate element wise sum
c = np.zeros(100)
for i in range(100):
    c[i] = a[i] + b[i]
print(c)


