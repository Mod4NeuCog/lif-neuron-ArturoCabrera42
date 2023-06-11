# IF network with time-awarenes
# This only takes into account refractory periods for individual neurons
# That is, the time when neurons can fire again.
import numpy as np

import time

class IF_Neuron:
    def __init__(self, refractory_period = 1.2):
        self.threshold = 0.75
        self.state = 0
        self.last_firing_time = 0
        self.refractory_period = refractory_period

    def activity(self, input_val, current_time):
        if input_val > self.threshold and (current_time - self.last_firing_time) > self.refractory_period:
            self.state = 1
            self.last_firing_time = current_time
        return self.state



class Layer(IF_Neuron):
    def __init__(self, units):
        self.units = units
        self.array = []

    # def generate_manual(self):
    #     for _ in range(self.units):
    #         neuron_input = float(input('Neuron state: '))
    #         neuron = IF_Neuron()
    #         neuron.activity(neuron_input)
    #         self.array.append(neuron)
    
    def generate_vec(self, input_vec, current_time):
        self.units = len(input_vec)
        self.array = [IF_Neuron() for _ in range(self.units)]
        for i in range(self.units):
            self.array[i].activity(input_vec[i], current_time)

    def visualize(self):
        print([neuron.state for neuron in self.array])


class Network(Layer):
    def __init__(self):
        self.web = []

    # def input_layer_manual(self):
    #     units = int(input("Neurons in the input layer: "))
    #     temp_layer = Layer(units)
    #     temp_layer.generate_manual()
    #     self.web.append(temp_layer)

    # def visualize_vertical(self):
    #     num_layers = len(self.web)
    #     num_neurons = max(layer.units for layer in self.web)

    #     # Print the layers vertically
    #     for i in range(num_neurons):
    #         layer_repr = ""
    #         for j in range(num_layers):
    #             if i < self.web[j].units:
    #                 layer_repr += str(self.web[j].array[i].state) + "\t"
    #             else:
    #                 layer_repr += "0\t"
    #         print(layer_repr)

    # action mechanism
    def visualize_vertical(self):
        num_layers = len(self.web)
        num_neurons = max(layer.units for layer in self.web)

        chosen_class = None
        max_activation = 0.0

        # Find the output neuron with the highest activation
        for i in range(num_neurons):
            for j in range(num_layers):
                if i < self.web[j].units and self.web[j].array[i].state > max_activation:
                    max_activation = self.web[j].array[i].state
                    chosen_class = i

            return chosen_class

    def interaction(self, input_layer, wm, current_time):
        vec_input = [float(neuron.state) for neuron in input_layer.array]

        if wm.shape[0] != len(vec_input):
            raise ValueError("Matrix and layer dimensions are not congruent.")

        temp_l = Layer(wm.shape[0])
        temp_w = wm.T

        weighted_i = np.zeros(len(vec_input))
        for i in range(wm.shape[0]):
            weighted_i[i] = np.sum(temp_w[:, i] * vec_input[i])

        for i in range(wm.shape[0]):
            neuron = IF_Neuron()
            neuron.activity(weighted_i[i], current_time)
            temp_l.array.append(neuron)

        self.web.append(temp_l)

weights = np.array([[0.6, 0.7, 0.8, 0.6, 0.7, 0.8], [0.01, 0.02, 0.06, 0.04, 0.05, 0.09], [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]])
weights = np.tile(weights, (2, 1))
input_layer = Layer(6)
current_time = time.time()
input_layer.generate_vec([1, 1, 1, 0, 1, 1], current_time)
charly = Network()
charly.web.append(input_layer)

for i in range(11):
    current_time = time.time()
    charly.interaction(charly.web[i], weights, current_time)
    if i % 3 == 0:
        np.random.shuffle(weights)

#charly.visualize_vertical()

# Obtain the predicted class from the network's final state
predicted_class = charly.visualize_vertical()
print("Predicted Class:", predicted_class)