import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import laplace

# Parameters see {tab:params}
lambda_weak = 0.5    # Weak coupling
lambda_critical = 1.5  # Critical phase
sigma = 1.0           # Localization scale [ly]
phi0 = 1.0            # Field amplitude
N = 100               # Spatial grid points
dt = 0.01             # Time step
steps = 1000          # Total steps


def simulate_delta_h(lambda_val):
    # Initialize fields
    x = np.linspace(-5*sigma, 5*sigma, N)
    phi = phi0 * np.exp(-x**2 / sigma**2)
    h = 0.1 * np.exp(-x**2 / (2*sigma)**2)  # Initial perturbation

    Gamma = np.sqrt(lambda_val) * phi0**2 / sigma

    for _ in range(steps):
        # Modified Einstein-PDE: dh/dt = -Γh + λφ²∇²h
        h += dt * (-Gamma * h + lambda_val * phi **
                   2 * laplace(h, mode='reflect'))

    return x, h


# Run simulations
x, h_weak = simulate_delta_h(lambda_weak)
x, h_critical = simulate_delta_h(lambda_critical)

# Plotting
plt.figure(figsize=(12, 5))

plt.subplot(121)
plt.plot(x, h_weak, 'r-', lw=2)
plt.title(f'Weak Coupling ($\\lambda = {lambda_weak}$)\nDivergence')
plt.xlabel('Spatial Coordinate $x$ [ly]')
plt.ylabel('$\\Delta h_{\\mu\\nu}$')

plt.subplot(122)
plt.plot(x, h_critical, 'b-', lw=2)
plt.title(f'Critical Phase ($\\lambda = {lambda_critical}$)\nStabilization')
plt.xlabel('Spatial Coordinate $x$ [ly]')

plt.tight_layout()
plt.savefig('phase_comparison.pdf', bbox_inches='tight')
