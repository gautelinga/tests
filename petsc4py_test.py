from petsc4py import PETSc

rank = PETSc.COMM_WORLD.Get_rank()
size = PETSc.COMM_WORLD.Get_size()

print "Process {rank} of {size}".format(rank=rank, size=size)
