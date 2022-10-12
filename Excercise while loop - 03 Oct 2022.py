# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 12:34:49 2022

@author: acabr
"""

import numpy as np
import matplotlib.pyplot as plt

dt=0.1
I=200
#typical neuron parameters
V_th = -65 #spike threshold
V_reset = -75 #reset potential
tau_m = 5 #membrane time constant
g_L= 10 # leak conductance
V_init = -75 #initial potential
E_L= -75 # leak reversal potential
global T #This global variable is defining for "how long" the simulation will run. Volt will work in terms of range(T), that is
#depending on for how many "seconds" you want this neuron to work
#2 Using a while loop

#---Beginning of model-----------------------------------------------------------------------
def dVolt(V_t_minus1):
    dV = (-(V_t_minus1-V_reset)+(I/g_L))/(tau_m)
    #print(dV)
    return dV

def Volt(size):
    V = []
    t = 0
    while t<=T-1: #we need to substract 1 so that x and y have the same dimensions
        #print(t)
        if t == 0:
            V.append(V_init)
        else:
            V.append(V[t-1]+dVolt(V[t-1])*dt)
            
        if V[t] > V_th:
            V[t] = V_reset
        t = t+1   #we go one step forward after all possible conditions have been evaluated

    return V
#---- End of model----------------------------------------

#---Beginning of simulator--------------------------------------------------------------------------          
T = int(input("Declare maximum time: "))
x = np.arange(0,T,1) #the size of X must be of the same size of T as well as Y so that they can be plotted
y = Volt(T) #same as above


plt.plot(x,y)
plt.show()

#---End of simulator-------------------------------------------------------------------------------
