import numpy



class NeuralNetwork:

    def __init__(self):
        numpy.random.seed(1)
        self.sypnapse_weights = 2 * numpy.random.random((3,1)) - 1
    
    def sigmoid_function(self, x):
        return 1 / (1 + numpy.exp(-x))
    
    def sigmoid_derivative_function(self, x):
        return x * (1 - x)
    
    def train(self, training_inputs, training_outputs, training_iterations):

        for i in range(training_iterations):

            output = self.compute(training_inputs)

            error = training_outputs - output

            adjustments = numpy.dot(training_inputs.T, error * self.sigmoid_derivative_function(output))

            self.sypnapse_weights += adjustments
    
    def compute(self, inputs):
        return self.sigmoid_function(numpy.dot(inputs.astype(float), self.sypnapse_weights))


if __name__ == "__main__":
    neural_network = NeuralNetwork()

    inputs = numpy.array([
        [5,0,1],
        [0,1,0],
        [1,0,0],
        [2,0,1]
    ])

    outputs = numpy.array([[1,1,0,0]]).T

    neural_network.train(inputs, outputs, 50000)

    input1 = str(input("Input for first index: "))
    input2 = str(input("Input for second index: "))
    input3 = str(input("Input for third index: "))

    output_prediction = neural_network.compute(numpy.array([input1,input2, input3]))
    print("The inputs are {0} ! ".format(numpy.array([input1,input2, input3])))

    print("I predict that the value is : {0}".format(int(numpy.round(output_prediction))))