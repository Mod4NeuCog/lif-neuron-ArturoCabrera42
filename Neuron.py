# coding=System
from array import *

class Neuron(object):

  """
   

  :version:
  :author:
  """

  """ ATTRIBUTES

   

  dt  (private)

   

  I  (private)

   

  tau_m  (private)

   

  g_L  (private)

   

  V_init  (private)

   

  E_L  (private)

   

  T  (private)

   

  V_th  (private)

   

  V_reset  (private)

  """

  def Volt(self, V):
    """
     

    @param array V : 
    @return float :
    @author
    """
    for t in range(T):
             if t == 0:
                 V.append(V_init)
             else:
                
                 V.append(V[t-1]+dVolt(V[t-1])*dt)
    
                    
             if V[t] > V_th:
                 V[t] = V_reset
                    
         return V


  def __dVolt(self, dV, V_t_minus1):
    """
     

    @param float dV : 
    @param float V_t_minus1 : 
    @return float :
    @author
    """
    dV = (-(V_t_minus1-V_reset)+(I/g_L))/(tau_m)




