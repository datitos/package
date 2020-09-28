import numpy as np

def sum(a, b):
    '''
    Returns the sum between "a" and "b"
    '''
    return a + b + 7

def matmul(a, b):
    '''
    Multiplies two matrix
    '''
    return np.matmul(a, b).tolist()
 
def substract(a,b):
    '''
    Calculates the difference between "a" and "b"
    '''
    return a - b

def hi():
    return 'Hello'
