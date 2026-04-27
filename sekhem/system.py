import numpy as np

class SEKHEMSystem:
    def __init__(self):
        self.dt = 0.01

    # Gradient of energy
    def gradV(self, X):
        return 2 * np.array(X)

    # Core controller (Phi + Omega)
    def u_core(self, X):
        return -1.0 * self.gradV(X)

    # Reflex controller (Psi)
    def u_reflex(self, X):
        return -2.0 * self.gradV(X)

    # Verification (simple version)
    def verification(self, X):
        v = np.dot(X, X)
        return np.exp(-v)

    # Step update
    def step(self, X):
        X = np.array(X)
        Veff = self.verification(X)

        if Veff < 0.2:
            u = self.u_reflex(X)
        else:
            uc = self.u_core(X)
            ur = self.u_reflex(X)
            u = Veff * uc + (1 - Veff) * ur

        X = X + self.dt * u
        return X.tolist()
