# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 10:07:04 2022

@author: acabr
"""

#Excercise of 6 Oct. 
#1)Simulate a neuron for t=0 to t=5 (seconds) using a for loop
#2) Add a while loop

#1 Using for loop

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

    
#---Beginning of model--------------------------------------------------------------------------------
def dVolt(V_t_minus1):
    dV = (-(V_t_minus1-V_reset)+(I/g_L))/(tau_m)
    #print(dV)
    return dV

def Volt(size):
    V = []
    for t in range(T):
        #print(t)
        if t == 0:
            V.append(V_init)
        else:
           
            V.append(V[t-1]+dVolt(V[t-1])*dt)

            
        if V[t] > V_th:
            V[t] = V_reset
        
    return V
#---Beginning of simulator--------------------------------------------------------------------------          
T = int(input("Declare maximum time: "))
x = np.arange(0,T,1) #the size of X must be of the same size of T as well as Y so that they can be plotted
y = Volt(T) #same as above


plt.plot(x,y)
plt.show()

#---End of simulator-------------------------------------------------------------------------------


