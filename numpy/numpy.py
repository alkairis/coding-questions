import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

# numpy products
print(numpy.dot(A,B))
print(numpy.cross(A,B))
print(numpy.inner(A,B))
print(numpy.outer(A,B))


# 
print(numpy.poly([1.1, 2, 3]))
print(numpy.roots([1.1, 2, 3]))
print(numpy.polyint([1.1, 2, 3]))
print(numpy.polyder([1.1, 2, 3]))
print(numpy.polyval([1.1, 2, 3], 0))
print(numpy.polyfit(A, B, 2))

# The NumPy module also comes with a number of built-in routines for linear algebra calculations. These can be found in the sub-module linalg.
# The linalg.det tool computes the determinant of an array.
print(numpy.linalg.det([A,B]))

# The linalg.eig computes the eigenvalues and right eigenvectors of a square array.
x,y = numpy.linalg.eig([A,B])
print(x)
print(y)

# The linalg.inv tool computes the (multiplicative) inverse of a matrix.
print(numpy.linalg.inv([A,B]))
print(numpy.linalg.det([[1.1, 1.1], [1.1, 1.2]]))