# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 00:43:02 2019

@author: tiwar
"""

import numpy as np
from constants import *
from init_condition import *

def f(t,x):
    
    if x[1]>np.arccos(a/D):
        x[1] = np.arccos(a/D)
    elif x[1]<-np.arccos(a/D):
        x[1] = -np.arccos(a/D)

    Q1 = -(-(w_s/2+w_p)*D*np.sin(x[0])+w_p*a*np.sin(x[0]-x[1]));
    Q2 = w_p*a*np.sin(x[0]-x[1]);

    a1 = I+m*D**2;
    b1 = m*D*a*np.cos(x[1]);
    c1 = Q1 + m*D*a*(x[3]**2)*np.sin(x[1]);
    
    a2 = m*D*a*np.cos(x[1]);
    b2 = m*a**2;
    c2 = Q2;
        
    x_dot = np.array([x[2], x[3], (b2*c1-b1*c2)/(a1*b2-a2*b1), (a1*c2-c1*a2)/(a1*b2-b1*a2)]);
    return x_dot