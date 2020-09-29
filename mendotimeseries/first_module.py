import numpy as np
import matplotlib.pyplot as plt

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
<<<<<<< HEAD
    
def max(list):
    '''
    Returns the max value in a list
    '''
    for c in list:
        maxVal = max(list)
    return (maxVal)

=======


def plot_random_walks():
    ''''
    Simulate 12 random walks, plot them.
    '''
    N = 100000
    random_walks = []

    plt.figure(figsize = (15,7))

    #Genera y grafica 12 random walks en el primer subplot
    f = plt.subplot(2, 1, 1)
    for i in range(12):
        random_walks.append(randomwalk(N))
        plt.plot(random_walks[i])
        plt.title('12 caminatas al azar')

    plt.xticks([])
    #Recupero los limites del primer subplot
    #asi los uso en los siguientes dos subplots
    ymin, ymax = f.get_ylim()

    #Busco los RW que mas y menos se alejan
    dic = {i:np.sum(abs(rw)) for i,rw in enumerate(random_walks)}
    menos_se_aleja = min(dic, key = dic.get)
    mas_se_aleja = max(dic, key = dic.get)

    #Plot del que menos se aleja
    plt.subplot(2, 2, 3)
    plt.plot(random_walks[menos_se_aleja])
    plt.ylim([ymin, ymax ])
    plt.xticks([])
    plt.title('Caminata que menos se aleja')

    #Plot del que mas se aleja
    plt.subplot(2, 2, 4)
    plt.plot(random_walks[mas_se_aleja])
    plt.ylim([ymin, ymax ])
    plt.xticks([])
    plt.title('Caminata que mas se aleja')

    plt.show()
>>>>>>> 007888c7f19e573a333434ce9f5ab2353df5c26c
