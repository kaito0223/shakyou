# -*- coding: utf-8 -*-
import numpy as np
import sys
sys.path.append('../common')
from function import softmax
from function import cross_entropy_error

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None    #loss
        self.y = None       #softmax output
        self.t = None       #training data (one-hot vector)

    def forword(self , x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)
        return self.loss

    def backword(self, dout=1):
        batch_size = self.t.shape[0] # the number of elements of t
        dx = (self.y - self.t)/batch_size
        return dx
