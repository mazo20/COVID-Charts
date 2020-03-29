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
R0 = 0
E0, I0, R0 = 200000, 50, 0 # Initial number of infected, Exposed, Recovered individuals, I0 and R0.
S0 = N - E0 - I0 - R0 #Everyone else, S0, is susceptible to infection initially.
r_0 = 2.2 #Basic reproduction number - Measure of contagiousness: the number of secondary infections each infected individual produces.
t_inc = 5.2 #Length of incubation period (in days)
t_inf = 2.9 #Duration of infectiousness (in days)
t_0 = 0
temp = 0

t_inf_c = 11.7-t_inc #Length from becoming infectious to being a confirmed case
proportion_of_deaths = 0.02 #proportion of confirmed cases
treshold = 37 #untill which time point, can we extrapolate values

my_data = genfromtxt('deaths_italy.csv', delimiter=',') #confirmed cases for Poland


"""Parameters to model"""
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta = r_0/t_inf
alpha = 1/t_inc
gamma = 1/t_inf
theta = proportion_of_deaths

# A grid of time points (in days)
t = np.linspace(0, treshold, treshold)


def sigmoid(t, t_0, a, temp):
    return a/(np.exp((t-t_0))/temp+1)


# The SEIR model differential equations.
def deriv(y, t, N, beta_0, alpha, gamma, t_0, temp):
    S, E, I, R = y    
    beta = sigmoid(t, t_0, beta_0, temp)
    
    
    
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - alpha * E
    dIdt = alpha * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt

# Initial conditions vector
y0 = S0, E0, I0, R0
# Integrate the SIR equations over the time grid, t.


def calculate_confirmed_array(beta_t, alpha_t, gamma_t, theta_t, y0, t_0, temp):
    ret = odeint(deriv, y0, t, args=(N, beta_t, alpha_t, gamma_t, t_0, temp))
    S, E, I, R = ret.T
    D=I*theta_t #confirmed cases are just proportion of infected cases shifted by some time
    #index_greater_than_one = np.where(C>=1.0)[0][0]
    #return C[index_greater_than_one:index_greater_than_one+24]
    return D

data_c = calculate_confirmed_array(beta, alpha, gamma, theta, y0, t_0, temp)
print(data_c)




def calculate_error(x):
    beta_t, E0, t_0_t, temp_t = x
    S0 = N - E0 - I0 - R0 #Everyone else, S0, is susceptible to infection initially.
    y0 = S0, E0, I0, R0
    
    model_data = calculate_confirmed_array(beta_t, alpha, gamma, theta, y0, t_0_t, temp_t)
    actual_data = my_data[1][:treshold]
    difference = model_data-actual_data
    error = np.dot(difference, difference)
    return error

#print(calculate_error(beta, alpha, gamma, theta))

p0 = [beta, E0, t_0, temp] 
print(p0)
bnds = ((0, None), (0, 4000), (1, 35), (1, None))
opt={"maxiter":10000}
results = minimize(calculate_error, p0, bounds=bnds, options=opt)
print(results)
params = results['x']
nbeta, nE0, nt_0, ntemp = params

ny0 = S0, nE0, I0, R0

data_c2 = calculate_confirmed_array(nbeta, alpha, gamma, theta, ny0, nt_0, ntemp)


nr_0 = nbeta/gamma
print("new r_0 =" + str(nr_0))

print("last r: " + str(sigmoid(37, nt_0, nbeta, ntemp)/gamma))




rs = sigmoid(t, nt_0, nbeta, ntemp)/gamma
print(rs)

plt.plot(t, rs)



#param, param_cov = curve_fit(calculate_confirmed_cases_at_time_t, my_data[0], my_data[1], p0) 


#t_c = t[]




# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)
#ax.plot(t_c, C, alpha=0.5, lw=2, label='Confirmed')
ax.plot(my_data[0], my_data[1], alpha=0.5, lw=2, label='Italy')
ax.plot(my_data[0][:treshold], data_c2, alpha=0.5, lw=2, label='Model')
#ax.plot(t, S, alpha=0.5, lw=2, label='Susceptible')
#ax.plot(t, E, alpha=0.5, lw=2, label='Exposed')
#ax.plot(t, I, alpha=0.5, lw=2, label='Infected')
#ax.plot(t, R, alpha=0.5, lw=2, label='Recovered with immunity')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number')
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()
