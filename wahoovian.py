import numpy as np
import logging

# Wahoovian Matrix Transformation

# the operation takes a square matrix and returns a square matrix with the same dimensions
# the output matrix will be the transpose of the input matrix, but with every value in the matrix negated

def wahoovian(matrix):
    #logging entering
    logging.info("Entering Wahoovian")

    # check if empty
    if matrix.size == 0:
        logging.info("Exiting Wahoovian")
        return matrix

    #check if square
    [c, r] = matrix.shape
    if not(r == c):
        logging.warning("Matrix is not square!")
        logging.info("Exiting Wahoovian")
        return matrix

    #transpose and negate
    else:
        print("reached third test")
        tMatrix = np.transpose(matrix)
        ntMatrix = np.negative(tMatrix)
        logging.info("Exiting Wahoovian")
        return ntMatrix
