# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 12:59:01 2020

@author: devin
"""

import numpy as np

matrix = np.array([[1, 2], [3, 4]])

print(matrix, "\n")

nMatrix = matrix.transpose()

print(nMatrix, "\n")

n2Matrix = np.negative(nMatrix)

print(n2Matrix)