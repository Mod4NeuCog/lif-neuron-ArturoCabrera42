# Algorithm 6
#Neuron simulation with inputs passed as comm args

class Neuron:
    def __init__(self):
        self.V_rest=-75
        self.V_threshold= -65
        self.V_membrane=-75
        self.spike=0
    
    def spikeCalc(self,argv):
        outputList = []
        for t in range(5):
            self.V_membrane = self.V_membrane+argv*t
            if self.V_membrane >= self.V_threshold:
                outputList.append(1)
            else:
                outputList.append(0)
        print(outputList) 

nc = float(input("Define neuron constant: "))
neuron = Neuron()
neuron.spikeCalc(nc)
