import numpy as np




class MSELoss:

    def forward(self, outputs, targets):
        """
        Computes MSE loss between outputs `outputs` and true targets `targets`.

        :param outputs: predicted outputs
        :param targets: true targets
        :return e: returns normalized mean squared error (by number of elements
        in outputs)
        """

        self.O = outputs
        self.Y = targets
        self.N = outputs.shape[0]
        self.q = outputs.shape[1]

        e = None




        return e


