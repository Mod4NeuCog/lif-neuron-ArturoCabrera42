# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:08:51 2022

@author: acabr
"""

# Whole umbrello 

#Define class Neuron with its specific atributes. Don't forget to use 
#self.attributes so every child can access to it
import numpy as np
import matplotlib.pyplot as plt

class Neuron:
    def __init__(self):
        self.dt=0.1
        self.I=200
        self.V_th=-65
        self.V_reset=-75
        self.tau_m=5
        self.g_L=10
        self.V_init=-75
        self.E_L=-75
        global T

    def dVolt(self,V_t_minus1):
        dV= (-(V_t_minus1-self.V_reset)+(self.I/self.g_L))/(self.tau_m)
        return dV
    
    def Volt(self,size):
        V = []
        for t in range(T):
            if t == 0:
                V.append(self.V_init)
            else:
            
                V.append(V[t-1]+self.dVolt(V[t-1])*self.dt)

                
            if V[t] > self.V_th:
                V[t] = self.V_reset
                
        return V

billy = Neuron() # Define that you have an object, called billy, that "behaves" like a neuron
T = int(input("Declare maximum time: "))
x = np.arange(0,T,1) #the size of X must be of the same size of T as well as Y so that they can be plotted
y = billy.Volt(T) #same as above


plt.plot(x,y)
plt.show()