import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib import pyplot
np.random.seed(41)

import Tensor


E0 = "ii"
E1 = "yi"
E2 = "iy"
#E3 = "iiyi"
#E4 = "iiiy"
#E5 = "iiiix"


Chars = [E0,E1,E2]


Errors = Tensor.Errorlist(Chars)

G = Tensor.Subspace(Errors)

u = 2**(len(Chars)-1)
H = np.zeros(shape=(u,u))

for i in range(len(G)):
    for j in range(len(G[0])):
        if(i <= j):
            H = np.add(H,G[i][j])

print(H)

