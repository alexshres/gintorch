import numpy as np


class Linear:

    def __init__(self, num_inputs, num_outputs):
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs

        # Weight matrix and bias vector
        # TODO: initialize weights to be zero-mean Gaussian
        # TODO: biases will be zero 
        self.W = None
        self.b = None


    def forward(self, A):
        """
        Performs operation y = AW + b
        :param A: Input data matrix 
        :return y: Output data matrix after affine transformation
        """

        self.A = A
        self.N = A.shape[0]
        y = None


        return y


    def backward(self, dLdy):
        """
        Backpropagation operation for variables in linear layer. Stores
        derivative dLdW, dLdb and returns dLdA

        :param dLdy: Derivative of loss with respect to output, obtained
        from backward operation on loss object
        :return dLDA: Derivative of loss with respect to input:
        """

        dydW = None
        dydb = None
        dydA = None
        dLdW = None
        dLdb = None
        dLdA = None

        self.dLdW = dLdW.T
        self.dLdb = dLdb.flatten()


        return dLdA
        

        
        
