"""
inbox.py
#########################
This file contains functions which I have implemented but do not know yet where to store them.

"""



import numpy as np




def rotation_matrix(angle:float):
    """
    If x is a column matrix. R@x    is a counter clockwise rotation of x.
    If x is a column matrix. R.T@x  is a         clockwise rotation of x.
    if x is a row matrix.    x@R    is a         cloxkwise rotation of x.
    if x is a row matrix.    x@R.T  is a counter cloxkwise rotation of x.
    """
    c,s = np.cos(angle), np.sin(angle)
    return np.array([[c, -s],
                     [s, c]])







