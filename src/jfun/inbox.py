"""
inbox.py
#########################
This file contains functions which I have implemented but do not know yet where to store them.

"""



import numpy as np

def is_angles_equal(angle_0:float, angle_1:float, tol:float=1e-10):
    # Returns if the angles are equal (as in modulo 2pi)
    angle_0_mod = angle_0 % 2*np.pi
    angle_1_mod = angle_1 % 2*np.pi
    return np.abs(angle_0_mod-angle_1_mod)<tol



def rotation_matrix(angle:float)->np.ndarray:
    """
    If x is a column matrix. R@x    is a counter clockwise rotation of x.
    If x is a column matrix. R.T@x  is a         clockwise rotation of x.
    if x is a row matrix.    x@R    is a         cloxkwise rotation of x.
    if x is a row matrix.    x@R.T  is a counter cloxkwise rotation of x.
    """
    c,s = np.cos(angle), np.sin(angle)
    return np.array([[c, -s],
                     [s, c]])



def angle_from_matrix(matrix:np.ndarray, tol: float = 1e-10)-> float:
    """
    Returns the angle of a rotation matrix. The angle is the angle which it rotates a vector (R@v).
    The angle returned is between -pi/2, and pi/2
    
    """
    
    assert matrix.ndim == 2, f"Expected array of dim 2, got {matrix.ndim}"
    assert np.all(matrix.shape == (2,2)), "Expected array of shape (2,2), got {matrix.shape}"
    assert np.abs(matrix[0,0]-matrix[1,1])<tol, "Expected diagonal elements to be equal"
    assert np.abs(matrix[1,0]+matrix[0,1])<tol, "Expected anti-diagonal to be opposite"
    assert np.all(np.abs(np.linalg.norm(matrix, axis = 0)-1) < tol), "Expected matrix to be unit"

    cos_angle = np.arccos((matrix[0,0]+matrix[1,1])/2.)
    sin_angle = np.arcsin((matrix[1,0]-matrix[0,1])/2.)
    
    if sin_angle < 0 and np.pi/2 < cos_angle:
        # Third quadrant
        cos_angle = -cos_angle
        sin_angle = -sin_angle-np.pi
    elif sin_angle < 0 and cos_angle < np.pi/2 :
        # Fourth quadrant
        cos_angle = -cos_angle
        sin_angle =  sin_angle
    elif 0 < sin_angle and  cos_angle < np.pi/2:
        # First quadrant
        cos_angle = cos_angle
        sin_angle = sin_angle
    elif 0 < sin_angle and np.pi/2 < cos_angle:
        # Second quadrant
        cos_angle = cos_angle
        sin_angle = -sin_angle+np.pi
    
    return (cos_angle+sin_angle)/2.





