import numpy as np

def sum(a, b):
    '''
    Returns the sum between "a" and "b"
    '''
    return a + b

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

def randomwalk(length):
    '''
    Returns a random walk of length = length
    '''
    pasos=np.random.randint (-1,2,length)
    return pasos.cumsum()
