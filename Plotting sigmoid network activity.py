# Plotting sigmoid network activity
import numpy as np
import matplotlib.pyplot as plt

class Sigmoid_Neuron:
    def __init__(self):
        self.state = 0
    
    def sigmoid(self, x):
        return (1/(1 + np.exp(-x)))
    
    def activity(self, input_value):
        self.state = self.sigmoid(input_value)
        return self.state

class Layer(Sigmoid_Neuron):
    def __init__(self, units=0):
        self.array = []
        self.units = units

    def generate_empty(self, units):
        """
        Defining a layer of "off" neurons
        """
        self.units = units #number of units
        self.array = [Sigmoid_Neuron() for _ in range(self.units)]
        #for i in range(self.units):
        #    self.array[i].activity(input_vec[i])

    def generate_vec(self, input_vec):
        """
        Defining a layer with given values for their states
        """
        self.units = len(input_vec)
        self.array = [Sigmoid_Neuron() for _ in range(self.units)]
        for i in range(self.units):
            self.array[i].state = input_vec[i]
    
    def visualize_layer(self):
        return np.array([neuron.state for neuron in self.array]) # Or print?

class Network(Layer):
    def __init__(self):
        self.web = []

    def visualize_network(self):
        """
        To visualize all of the layers in the network vertically, with values 
        rounded up to 4 decimals.
        """
        num_layers = len(self.web)
        num_neurons = max(layer.units for layer in self.web)

        # Print the layers vertically
        for i in range(num_neurons):
            layer_repr = ""
            for j in range(num_layers):
                if i < self.web[j].units:
                    layer_repr += f"{round(self.web[j].array[i].state, 4):.4f}\t"
                else:
                    layer_repr += "0.0000\t"
            print(layer_repr)


    def interaction(self, input_layer, wm):
        """
        Interaction between layers. Needs a weights matrix.
        """
        vec_input = [float(neuron.state) for neuron in input_layer.array]

        if wm.shape[0] != len(vec_input):
            raise ValueError("Matrix and layer dimensions are not congruent.")

        temp_l = Layer(wm.shape[0])
        temp_w = wm.T

        weighted_i = np.zeros(len(vec_input))
        for i in range(wm.shape[0]):
            weighted_i[i] = np.sum(temp_w[:, i] * vec_input[i])

        for i in range(wm.shape[0]):
            neuron = Sigmoid_Neuron()
            neuron.activity(weighted_i[i])
            temp_l.array.append(neuron)

        self.web.append(temp_l)

    def plot_activity(self):
        act = np.empty([max(layer.units for layer in self.web), len(self.web)])
        # Empty layer where each row is a neuron, each column a layer
        for i in range(len(self.web)):
            act[:,i] = self.web[i].visualize_layer().T

        num_rows, num_cols = act.shape

        fig, axes = plt.subplots(num_rows, 1, figsize=(8, 6), sharex=True)

        # Iterate over each row and plot it in a separate subplot
        cols = ["blue", "red", "orange", "green", "purple", "olive"]
        for i in range(num_rows):
            axes[i].plot(act[i], color = cols[i])
            axes[i].set_ylabel(f'Neuron {i+1}')
    
        axes[-1].set_xlabel('Layer')
        plt.tight_layout()
        plt.show()



charly = Layer()
charly.generate_vec([0.2, -0.5, 0.8, -0.1, 0.9, 0])

lily = Network()
lily.web.append(charly)

# weights = np.array([[0.1, 0.01, 0.3],
#                     [0.0001, 0.2, 0.001],
#                     [-0.5, -0.3, -0.6]])

weights = np.array([[0.6, 0.7, 0.8, 0.6, 0.7, 0.8], [0.01, 0.02, 0.06, 0.04, 0.05, 0.09], [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]])
weights = np.tile(weights, (2, 1))

for i in range(10):
    lily.interaction(lily.web[i], weights)
    if i % 2 ==0:
        np.random.shuffle(weights)
#lily.interaction(lily.web[1], weights2)

lily.plot_activity()



