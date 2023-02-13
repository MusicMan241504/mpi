from mpi4py import MPI
import random as rand
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


#Each node will preform a differnt thing to a number
#All commands will be sent from node 0


if rank == 0:
    num = 1
    count = 0

    start = time.time()

    while count < 1000000:
        node = rand.randint(1,size-1)
        comm.send(num,dest=node)
        num = comm.recv(source=node)
        count+=1
        #print(num)
        #time.sleep(1)

    end = time.time()
    print(end-start)



if rank == 1:
    while True:
        num = comm.recv(source=0)
        num = num*2
        comm.send(num,dest=0)

if rank == 2:
    while True:
        num = comm.recv(source=0)
        num = num+5
        comm.send(num,dest=0)

if rank == 3:
    while True:
        num = comm.recv(source=0)
        num = num%100
        comm.send(num,dest=0)

if rank == 4:
    while True:
        num = comm.recv(source=0)
        num = num%10
        comm.send(num,dest=0)

if rank == 5:
    while True:
        num = comm.recv(source=0)
        num = num%50
        comm.send(num,dest=0)

if rank == 6:
    while True:
        num = comm.recv(source=0)
        num = num**2
        comm.send(num,dest=0)

if rank == 7:
    while True:
        num = comm.recv(source=0)
        num = num*-1
        comm.send(num,dest=0)
