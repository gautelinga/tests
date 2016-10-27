from mpi4py import MPI
import h5py
 
rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size
 
f = h5py.File('parallel_test.hdf5', 'w', driver='mpio', comm=MPI.COMM_WORLD)
 
dset = f.create_dataset('test', (size,), dtype='i')
dset[rank] = rank
 
f.close()
