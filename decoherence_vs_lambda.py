import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Quantum master equation with constraint strength λ


def decoherence_model(rho, t, λ):
    gamma = 0.1 * λ**2  # Decoherence rate proportional to λ²
    return -gamma * (rho - np.diag(np.diag(rho)))  # Lindblad form


# Parameters
λ_range = np.linspace(0, 5, 50)
times = np.linspace(0, 10, 100)
rho0 = np.array([[0.5, 0.5], [0.5, 0.5]])  # Initial superposition state

# Simulation
branching_probs = []
for λ in λ_range:
    solution = odeint(decoherence_model, rho0.flatten(), times, args=(λ,))
    final_rho = solution[-1].reshape((2, 2))
    branching_probs.append(np.abs(final_rho[0, 1]))  # Off-diagonal survival

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(λ_range, branching_probs, 'b-', linewidth=2)
plt.xlabel('Constraint Strength (λ)', fontsize=14)
plt.ylabel('Timeline Branching Probability', fontsize=14)
plt.title('Quantum Decoherence vs FPIT Constraint Strength', fontsize=16)
plt.grid(True)
plt.savefig('decoherence_vs_lambda.pdf', dpi=300, bbox_inches='tight')
