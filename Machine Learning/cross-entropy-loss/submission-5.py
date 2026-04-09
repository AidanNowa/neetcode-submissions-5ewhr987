import numpy as np
from numpy.typing import NDArray


class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: true labels (0 or 1)
        # y_pred: predicted probabilities
        # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
        # return round(your_answer, 4)
        y_pred = y_pred + np.exp(-16)
        total = 0
        for i in range(len(y_true)):
            total += (y_true[i] * np.log(y_pred[i])) + ((1-y_true[i])*np.log(1-y_pred[i]))
        return np.round(-1/len(y_true) * total, 4)

    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: one-hot encoded true labels (shape: n_samples x n_classes)
        # y_pred: predicted probabilities (shape: n_samples x n_classes)
        # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
        # return round(your_answer, 4)
        y_pred = y_pred + np.exp(-16)
        total = 0
        for i in range(len(y_true)):
            sub_total = 0
            for j in range(len(y_pred[0])):
                sub_total += y_true[i][j] * np.log(y_pred[i][j])
            total += sub_total
        return np.round(-1/len(y_true) * total, 4)

