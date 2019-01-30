import numpy
myarray = numpy.array([[ 2, -1, 0, 0, -1, 0],
                       [ -1, 3, -1, 0, -1, 0],
                       [ 0, -1, 2, -1, 0, 0],
                       [0 ,0 ,-1 ,3 ,-1, -1],
                       [-1, -1, 0, -1, 3, 0],
                       [0, 0, 0, -1, 0, 1]])
e_values, e_vectors = numpy.linalg.eig(myarray)
print(e_vectors) # the i-th eigenvector is the i-th *column* of this matrix
print(e_values) # the i-th eigenvalue is the i-th element of this vector

