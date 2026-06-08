"""
Single-Layer Feedforward Neural Network
========================================
Architecture:
    Input (n) ──→ [W, b] ──→ Output (k)

No hidden layers. One weight matrix. One bias vector.
This is equivalent to logistic regression (with sigmoid)
or linear regression (without activation).
"""

import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -500, 500)))


class SingleLayerNN:
    """
    Parameters
    ----------
    n_inputs  : number of input features
    n_outputs : number of output neurons
    seed      : random seed for reproducibility
    """

    def __init__(self, n_inputs: int, n_outputs: int, seed: int = 42):
        self.n_inputs  = n_inputs
        self.n_outputs = n_outputs

        rng = np.random.default_rng(seed)

        self.W = rng.standard_normal((n_inputs, n_outputs)) * np.sqrt(1.0 / n_inputs)
        self.b = np.zeros(n_outputs)

    def forward(self, X: np.ndarray) -> np.ndarray:
        """
        Forward pass: z = X·W + b  →  ŷ = sigmoid(z)

        X     : shape (batch_size, n_inputs)
        returns: shape (batch_size, n_outputs)
        """
        z = X @ self.W + self.b     
        return sigmoid(z)

    def summary(self):
        print("=" * 45)
        print("  Single-Layer Feedforward Neural Network")
        print("=" * 45)
        print(f"  Input → Output : {self.n_inputs} → {self.n_outputs}")
        print(f"  W shape        : {self.W.shape}")
        print(f"  b shape        : {self.b.shape}")
        print(f"  Total params   : {self.W.size + self.b.size}")
        print("=" * 45)
        print(f"\n  W | mean={self.W.mean():+.4f}  std={self.W.std():.4f}"
              f"  min={self.W.min():+.4f}  max={self.W.max():+.4f}")
        print(f"  b | {self.b}")


if __name__ == "__main__":
    net = SingleLayerNN(n_inputs=4, n_outputs=1, seed=42)
    net.summary()

    X = np.random.default_rng(0).standard_normal((5, 4))
    y_hat = net.forward(X)

    print("\n  Sample predictions ŷ:")
    print(np.round(y_hat, 4))