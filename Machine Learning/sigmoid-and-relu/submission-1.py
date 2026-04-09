import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        sigmoid_array = []
        for ele in z:
            sigmoid_array.append(round((1/(1+np.exp(-1*ele))),5))
        return sigmoid_array

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        relu_array = []
        for ele in z:
            relu_array.append(round(max(0.0,ele),5))
        return relu_array
