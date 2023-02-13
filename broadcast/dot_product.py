from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    a = np.random.randint(100,size=100,dtype='i')
    b = np.random.randint(100,size=100,dtype='i')
else:
    a = np.empty(100,dtype='i')
    b = np.empty(100,dtype='i')

comm.Bcast(a,root=0)
comm.Bcast(b,root=0)

c = np.empty(100,dtype='i')
for i in range(100):
    c[i] = a[i] * b[i]
result = np.sum(c)
print(result)

