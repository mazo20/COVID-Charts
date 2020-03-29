#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:32:31 2020

@author: wojtekadamczyk
"""

import numpy as np 
  
# curve-fit() function imported from scipy 
from scipy.optimize import curve_fit

x = np.linspace(0, 1, num = 40) 
  
y = 3.45 * np.exp(1.334 * x) + np.random.normal(size = 40) 
  
def test(x, a, b): 
    return a*np.exp(b*x) 
  
param, param_cov = curve_fit(test, x, y) 

print(param)
print(param_cov)