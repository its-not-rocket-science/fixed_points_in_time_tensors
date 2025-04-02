import numpy as np
import matplotlib.pyplot as plt

# Analytic solution for coherence decay
λ_range = np.linspace(0, 5, 100)
initial_coherence = 0.5  # Initial superposition strength
simulation_time = 10     # Total evolution time

# Compute branching probability: P = |coherence| = 0.5 * e^(-λ * 0.1 * t)
branching_probs = initial_coherence * np.exp(-0.1 * λ_range * simulation_time)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(λ_range, branching_probs, 'b-', linewidth=2)
plt.yscale('log')
plt.ylim(1e-3, 1)
plt.xlabel('Constraint Strength (λ)', fontsize=14)
plt.ylabel('Timeline Branching Probability', fontsize=14)
plt.title('Quantum Decoherence vs FPIT Constraint Strength', fontsize=16)
plt.grid(True)
plt.savefig('decoherence_vs_lambda.pdf', dpi=300, bbox_inches='tight')
