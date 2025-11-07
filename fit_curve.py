import numpy as np
import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("xy_data.csv")
x_data = data["x"].values
y_data = data["y"].values

# Generate t values
t_values = np.linspace(6, 60, len(x_data))

# Equations
def curve_equations(params, t):
    theta, M, X = params
    x_pred = t * np.cos(theta) - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta) + X
    y_pred = 42 + t * np.sin(theta) + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    return x_pred, y_pred

# Loss function
def loss(params):
    x_pred, y_pred = curve_equations(params, t_values)
    return np.sum(np.abs(x_data - x_pred) + np.abs(y_data - y_pred))

# Initial values and ranges
initial_guess = [np.deg2rad(25), 0, 50]
bounds = [(np.deg2rad(0), np.deg2rad(50)), (-0.05, 0.05), (0, 100)]

res = minimize(loss, initial_guess, bounds=bounds, method='L-BFGS-B')
theta_opt, M_opt, X_opt = res.x

print("Optimized parameters:")
print("θ =", round(theta_opt, 4), "radians")
print("M =", round(M_opt, 4))
print("X =", round(X_opt, 4))

# Plot and save
x_pred, y_pred = curve_equations([theta_opt, M_opt, X_opt], t_values)
plt.figure(figsize=(8,6))
plt.scatter(x_data, y_data, label="Actual data", alpha=0.7)
plt.plot(x_pred, y_pred, color="red", label="Fitted curve", linewidth=2)
plt.xlabel("x"); plt.ylabel("y"); plt.legend(); plt.title("Curve Fit Result")
plt.savefig("fitted_curve.png")
plt.show()
