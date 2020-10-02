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
    m = len(matrix[0])
    n = matrix.size

    if not(m == n):
        logging.warning("Matrix is not square!")
        logging.info("Exiting Wahoovian")
        return matrix

    #transpose and negate
    else:
        matrix.transpose()
        np.negative(matrix)
        logging.info("Exiting Wahoovian")
        return matrix

