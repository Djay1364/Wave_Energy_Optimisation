# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 01:09:11 2019

@author: tiwar
"""

import numpy as np
from constants import *
from init_condition import *
from dynamics import f
from RK4_solver import solver
import matplotlib.pyplot as plt

#initialize
alpha = alpha0
beta = beta0
alpha_dot = alpha_dot0
beta_dot = beta_dot0
h = 0.1 #integration time step

x = np.array([alpha,beta,alpha_dot,beta_dot])
t = 0

q1 = []
q2 = []
q1_dot = []
q2_dot = []
time = []

for i in range(1000):
    x = solver(f,x,t,h)
    q1.append(x[0])
    q2.append(x[1])
    q1_dot.append(x[2])
    q2_dot.append(x[3])
    t = t+h  
    time.append(t)

plt.plot(time,q1,'b',label = 'alpha')
plt.plot(time,q2,'r',label = 'beta')
plt.plot(time,q1_dot,'y',label = 'alpha_dot')
plt.plot(time,q2_dot,'g',label = 'beta_dot')
plt.legend()
plt.show()
     