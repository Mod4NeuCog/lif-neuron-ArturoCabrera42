#Algorithm 7
class Neuron:
    def __init__(self):
        self.V_rest=-75
        self.V_threshold= -65
        self.V_membrane=-75
        self.spike=0
        self.t=1
    
    def __main__(self,argv):
        outputSpike = []
        while self.t <= 5:
            self.V_membrane = self.V_membrane+argv*self.t
            if self.V_membrane >= self.V_threshold:
                self.spike=1
                outputSpike.append(self.spike)
            else:
                self.spike=0
                outputSpike.append(self.spike)
            self.t = self.t+1
        print(outputSpike)
        
nc = float(input("Define neuron constant: "))
neuron = Neuron()
neuron.__main__(nc)