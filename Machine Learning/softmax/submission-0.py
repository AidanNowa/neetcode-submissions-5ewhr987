import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        total = 0
        for ele in z:
            total += np.exp(ele-max(z))
        probs = []
        for ele in z:
            prob = np.exp(ele-max(z)) / total
            probs.append(prob)
        return np.round(probs, 4)
