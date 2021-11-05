

import jfun
from jfun.inbox import angle_from_matrix
import numpy as np

def test_rotation_matrix():
    from jfun.inbox import rotation_matrix
    tol = 1e-10

    # Test 0
    # Basic test
    ## Run
    angle = 0
    R = rotation_matrix(angle)
    ## Asserted answere
    R_ = np.array([[1,0],[0,1]])
    assert np.all(np.abs(R-R_)<tol), "Failed 'Test 0'"
    
    # Test 1
    # Positiv angle
    ## Run
    angle = np.pi/3
    R = rotation_matrix(angle)
    ## Asserted answere
    c,s = np.cos(angle), np.sin(angle)
    R_ = np.array([[c,-s],[s,c]])
    assert np.all(np.abs(R-R_)<tol), "Failed 'Test 1'"
    
    # Test 2
    # Negative angle
    ## Run
    angle = -np.pi/3
    R = rotation_matrix(angle)
    ## Asserted answere
    c,s = np.cos(angle), np.sin(angle)
    R_ = np.array([[c,-s],[s,c]])
    assert np.all(np.abs(R-R_)<tol), "Failed 'Test 2'"
    
    # Test 3
    # With angle from matrix
    ## Run
    for angle in np.linspace(-np.pi, np.pi,360):
        R = rotation_matrix(angle)
        angle_ = angle_from_matrix(R)
        angle_mod = angle % 2*np.pi
        angle_mod_ = angle_ % 2*np.pi
        assert np.abs(angle-angle_)< tol, f"Failed test 3.\nInput angle: {angle/(2*np.pi)*360} degrees, Output angle {angle_/(2*np.pi)*360} degrees"

    return 0






if __name__ == '__main__':
    test_rotation_matrix()
    print("Rotation Matrix passed the test")
    




