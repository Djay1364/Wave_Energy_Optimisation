# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 00:48:06 2019

@author: tiwar
"""

import numpy as np
from constants import *
from init_condition import *
from dynamics import f

def solver(f,x,t,h):
    
    k1 = f(t,x)
    k2 = f(t+h/2,x+h*k1/2)
    k3 = f(t+h/2,x+h*k2/2)
    k4 = f(t+h,x+k3)
    
    x = x+h*(k1+2*(k2+k3)+k4)/6
    
    if x[1]>np.arccos(a/D):
        x[1] = np.arccos(a/D)
    elif x[1]<-np.arccos(a/D):
        x[1] = -np.arccos(a/D)
    
    
    return x