import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib import pyplot
np.random.seed(41)

X = np.matrix([[0,1],[1,0]])
Y = np.matrix([[0,-1j],[1j,0]])
Z = np.matrix([[1,0],[0,-1]])
I = np.matrix([[1,0],[0,1]])


#  WLOG we can write errors as an arbitrary product of Pauli X Y Z and I
#  Tensorcompute takes a string char of 'xyiziiy' pauli matrices and computes the 
#  Product of this string of errors as a 2^(length(char)) matrix

def Tensorcompute(char):
    
    if(char[0]=="i"):
        A = I
    elif(char[0]=="x"):
        A = X
    elif(char[0]=="y"):
        A = Y
    elif(char[0]=="z"):
        A = Z

    for i in range(len(char)-1):
        
        if(char[1+i]=="i"):
            P = I
        elif(char[1+i]=="x"):
            P = X
        elif(char[1+i]=="y"):
            P = Y
        elif(char[1+i]=="z"):
            P = Z

        Q = np.kron(A,P)
        A = Q

    return A


def Errorlist(charlist):
    x = len(charlist)
    y = 2**len(charlist[0])
    K = np.zeros(shape=(x,y,y),dtype=complex)
    for i in range(len(charlist)):
        K[i] = np.matrix(Tensorcompute(charlist[i]))
        

    return K

def Subspace(K):

    G = np.zeros(shape = (len(K),len(K),len(K[0]),len(K[0])),dtype=complex)

    for i in range(len(K)):
        for j in range(len(K)):
            G[i,j] = np.matmul(K[i],np.matrix(K[j]).getH())
            
    return G


