import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib import pyplot
np.random.seed(41)

import Tensor


E0 = "iiii"
E1 = "xiii"
E2 = "ixii"
E3 = "iixi"
E4 = "iiix"
#E5 = "iiiix"

Chars = [E0,E1,E2,E3,E4]

Errors = Tensor.Errorlist(Chars)

G = Tensor.Subspace(Errors)

u = 2**(len(Chars)-1)
H = np.zeros(shape=(u,u))

for i in range(len(G)):
    for j in range(len(G[0])):
        if(i < j):
            H = np.add(H,G[i][j])
            
H = np.add(H,TensorCompute(E0))
            
print(H)

