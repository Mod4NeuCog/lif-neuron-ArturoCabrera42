# 19 Oct 2022
#1 instantiate neurons, each with different values for its membrane threshold and store them in a table
#2 Create another list, with the same number of elements as the list of neurons
#3 this new list will store "electric inputs", maybe generate them randomly
#4 Create class axon which will loop a comparison:
#       for neuron1 in my list of neurons, compare with its correspondent input, input1. if it is enough to fire, then the axon of this specific neuron fired
#       store this as a 1 in a list of the same dimension as that of the neurons. If it did not fire, store a 0
import random

global number_neurons #number of neurons to be asked to the user

class Neuron(): #will generate a list of n neurons with different threshold potentials
    def __init__(self):
      self.list_neurons = [] #List where the threshold of each neuron will be stored

    def generateNeurons(self, number):
        self.list_neurons = [] #List where the threshold of each neuron will be stored
        for i in range(number):
            self.list_neurons.append(random.randint(-80, -40))
            #each number will represent the potential threshold of each neuron
        return self.list_neurons
    
    def getListNeurons(self):
        return self.list_neurons


class Dendrite(): #will generate a list of same size as that of neurons of random inputs
    def __init__(self):
        self.list_inputs=[] #list where the inputs towards each neuron will be stored
    
    def generateInputs(self, number):
        for i in range(number):
            self.list_inputs.append(random.randint(-60, -10))
            #each number represents the input for reach neuron
        return self.list_inputs
    
    def getListInputs(self):
        return self.list_inputs
            

class Axon(): #will compare the thresholds of neurons and dendrites and check if neurons fired, store results in a list and prints!
    def _init__(self):
        self.list_results=[] #list where the results (1 if fired, 0 if not) will be stored
    
    def axonFired(self, number, neurons, dendrites):
        self.list_results=[] #list where the results (1 if fired, 0 if not) will be stored

        for i in range(number):
            if neurons.list_neurons[i] < dendrites.list_inputs[i]:
                self.list_results.append(1)
            else:
                self.list_results.append(0)
        return self.list_results

    def getListResults(self):
        return self.list_results #function to retrieve the list of results
        
numberNeurons = int(input("Define the number of neurons in your network: "))
list_neurons=Neuron()
list_neurons.generateNeurons(numberNeurons)
list_inputs=Dendrite()
list_inputs.generateInputs(numberNeurons)
list_outputs=Axon()
list_outputs.axonFired(numberNeurons,list_neurons,list_inputs)
print("List of neurons' thresholds")
print(list_neurons.getListNeurons())

print("List of inputs")
print(list_inputs.getListInputs())

print("Neurons that fired")
print(list_outputs.getListResults()) #actually printing the outputs



