# -*- coding: utf-8 -*-
import numpy as np
from mnist import load_mnist

def get_data():
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(flatten=True, normalize=True, one_hot_label=False)
