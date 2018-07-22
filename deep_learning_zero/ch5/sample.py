# -*- coding: utf-8 -*-
import numpy as np


X = np.random.rand(2) #input
W = np.random.rand(2,3) #weight
B = np.random.rand(3) #bias

print(X)
print(W)
print(B)

Y=np.dot(X,W)+B

print(Y)
