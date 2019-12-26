import numpy

def sigmoid(x):
    return 1 / (1 + numpy.exp(-x))

def sigmoid_derivatives(x):
    return x * (1 - x)
inputs = numpy.array(
    [[0,1,0],
    [0,1,1],
    [1,1,1],
    [1,1,0]])

expected_outputs = numpy.array([[0,0,1,1]]).T

numpy.random.seed(1)

synapse_weights = 2 * numpy.random.random((3, 1)) - 1

print('Synapse weights: {0}'.format(synapse_weights))

for iteration in range(50000):
    input_layer = inputs

    outputs = sigmoid(numpy.dot(input_layer, synapse_weights))

    error = expected_outputs - outputs
    adjustments = error * sigmoid_derivatives(outputs)
    synapse_weights += numpy.dot(input_layer.T, adjustments)


print('Synapse weights after Training: {0}'.format(synapse_weights))

print('Outputs {0}'.format(outputs))