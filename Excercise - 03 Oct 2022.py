# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:40:17 2022

@author: acabr
"""

#Excercise 1, intro to programming
#Simulate a LIF neuron for 100s with dt=0.1 When V = V_th reset value to V_reset

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

    
#---Beginning of model--------------------------------------------------------------------------------
def dVolt(V_t_minus1):
    dV = (-(V_t_minus1-V_reset)+(I/g_L))/(tau_m)
    #print(dV)
    return dV

def Volt(size):
    V = []
    for t in range(1000):
        #print(t)
        if t == 0:
            V.append(V_init)
        else:
           
            V.append(V[t-1]+dVolt(V[t-1])*dt)
            #print(dVolt(t)*dt)
            
        if V[t] > V_th:
            V[t] = V_reset
        
    return V

#---End of model------------------------------------------------------------------------------------

#---Beginning of simulator--------------------------------------------------------------------------          
x = np.arange(0,100,0.1)
y = Volt(1000)


plt.plot(x,y)
plt.show()

#---End of simulator-------------------------------------------------------------------------------
