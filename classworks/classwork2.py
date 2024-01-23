# Gauss-Jordan Method

import numpy as np

# add row
def add_row(A,m,i,j):
    
    '''
    m: multiplier
    Add m times row j to row i in a matrix A
    '''
    # n stores the the size of a matrix A of size n x n
    n = A.shape[0] # row dimension of A
    E = np.eye(n) # nxn identity matrix
    if i==j:
        E[i,j] = m + 1
    else:
        E[i,j] = m
    return E @ A

# swap-rows
def swap_rows(A,i,j):
    '''
    Interchange rows i and j of a matrix A
    Note the identity matrix E is always a square matrix
    Swap rows of identity matrix E to interchange rows of A
    Returns E @ A
    '''
    n = A.shape[0]
    E = np.eye(n)
    E[i,i] = 0
    E[j,j] = 0
    E[i,j] = 1
    E[j,i] = 1
    return E @ A

# scale-row
def scale_row(A,s,i):
    '''
    A: a matrix 
    s: scale factor
    Multiply row i of A by scale factor s
    '''
    n = A.shape[0]
    E = np.eye(n)
# [i,i] is the index of diagonal element of row i that is scaled by s
    E[i,i] = s
    return E @ A

Y = np.array([[5,4,2],[-1,2,1],[1,1,1]])

I = np.array([[1,0,0],[0,1,0],[0,0,1]])

A = np.hstack((Y,I))

A2 = scale_row(A,1/5,0)

A3 = add_row(A2,1,1,0)

A4 = add_row(A3,-1,2,0)

A5 = scale_row(A4,1/2.8,1)

A6 = add_row(A5,-0.2,2,1)

A7 = scale_row(A6, 1/0.5, 2)

A8 = add_row(A7,-0.5,1,2)

A9 = add_row(A8,-0.4,0,2)

A10 = add_row(A9,-0.8,0,1)

A_ = np.linalg.inv(Y)
A_
np.round(A10,2)
