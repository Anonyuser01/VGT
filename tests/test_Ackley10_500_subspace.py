# -*- coding: utf-8 -*-

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import numpy as np
from benchmarks.synthetic_functions import Ackley10_500


if os.path.exists('result.csv'):
    os.remove('result.csv')


dims = 500
lb = np.zeros(dims)
ub = np.ones(dims)

f = Ackley10_500 

n_init = 10
max_iter = 1050
N_neighbor = 20
Cp = 0.1

use_subspace = True
_Rp = 1

from VGT import VGT



agent = VGT(f,lb,ub,n_init,max_iter,N_neighbor=N_neighbor,Cp= Cp,use_subspace=use_subspace,_Rp=_Rp)
agent.search()



