#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:10:47 2020

@author: wojtekadamczyk
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from numpy import genfromtxt



"""INPUT DATA"""
N = 60500000 # Total population, N.
E0, I0, R0 = 200, 62, 0 # Initial number of infected, Exposed, Recovered individuals, I0 and R0.
S0 = N - E0 - I0 - R0 #Everyone else, S0, is susceptible to infection initially.
r_0 = 2.2 #Basic reproduction number - Measure of contagiousness: the number of secondary infections each infected individual produces.
t_inc = 5.2 #Length of incubation period (in days)
t_inf = 2.9 #Duration of infectiousness (in days)

t_inf_c = 11.7-t_inc #Length from becoming infectious to being a confirmed case
proportion_of_confirmed = 0.2 #proportion of confirmed cases

my_data = genfromtxt('italy_data.csv', delimiter=',') #confirmed cases for Poland


"""Parameters to model"""
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta = r_0/t_inf
alpha = 1/t_inc
gamma = 1/t_inf
theta = proportion_of_confirmed

# A grid of time points (in days)
t = np.linspace(0, 35, 35)

# The SEIR model differential equations.
def deriv(y, t, N, beta, alpha, gamma):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - alpha * E
    dIdt = alpha * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt

# Initial conditions vector
y0 = S0, E0, I0, R0
# Integrate the SIR equations over the time grid, t.


def calculate_confirmed_array(beta_t, alpha_t, gamma_t, theta_t, y0):
    ret = odeint(deriv, y0, t, args=(N, beta_t, alpha_t, gamma_t))
    S, E, I, R = ret.T
    C=I*theta_t #confirmed cases are just proportion of infected cases shifted by some time
    #index_greater_than_one = np.where(C>=1.0)[0][0]
    #return C[index_greater_than_one:index_greater_than_one+24]
    return C

data_c = calculate_confirmed_array(beta, alpha, gamma, theta, y0)
print(data_c)




def calculate_error(x):
    beta_t, alpha_t, gamma_t, theta_t, E0 = x
    I0, R0 = 62, 0 # Initial number of infected, Exposed, Recovered individuals, I0 and R0.
    S0 = N - E0 - I0 - R0 #Everyone else, S0, is susceptible to infection initially.
    y0 = S0, E0, I0, R0
    
    model_data = calculate_confirmed_array(beta_t, alpha_t, gamma_t, theta_t, y0)
    actual_data = my_data[1]
    difference = model_data-actual_data
    error = np.dot(difference, difference)
    return error

#print(calculate_error(beta, alpha, gamma, theta))

p0 = [beta, alpha, gamma, theta, 200] 
print(p0)
bnds = ((0, 1.2), (0.05, None), (0.05,None), (0,1), (0, 4000))
opt={"maxiter":10000}
results = minimize(calculate_error, p0, bounds=bnds, options=opt)
print(results)
params = results['x']
nbeta, nalpha, ngamma, ntheta, nE0 = params

ny0 = S0, nE0, I0, R0

data_c2 = calculate_confirmed_array(nbeta, nalpha, ngamma, ntheta, ny0)





#param, param_cov = curve_fit(calculate_confirmed_cases_at_time_t, my_data[0], my_data[1], p0) 


#t_c = t[]




# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)
#ax.plot(t_c, C, alpha=0.5, lw=2, label='Confirmed')
ax.plot(my_data[0], my_data[1], alpha=0.5, lw=2, label='Italy')
ax.plot(my_data[0], data_c2, alpha=0.5, lw=2, label='Model')
#ax.plot(t, S, alpha=0.5, lw=2, label='Susceptible')
#ax.plot(t, E, alpha=0.5, lw=2, label='Exposed')
#ax.plot(t, I, alpha=0.5, lw=2, label='Infected')
#ax.plot(t, R, alpha=0.5, lw=2, label='Recovered with immunity')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number (1000s)')
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()
