# -*- coding: utf-8 -*-
import numpy as np

def softmax(a):
    c=np.max(a)
    exp_a = np.exp(a-c) #preclude overflow 
    sum_exp_a = np.sum(exp_a)
    y=exp_a / sum_exp_a
    
    return y


def cross_entropy_error(y, t):
    delta =1e-7
    return -np.sum(t * np.log(y + delta))