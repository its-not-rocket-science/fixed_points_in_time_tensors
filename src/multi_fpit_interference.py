import numpy as np
import matplotlib.pyplot as plt


def multi_fpit_interaction(x, σ1, σ2, λ):
    # Two Gaussian constraint fields
    ϕ1 = np.exp(-(x - 5)**2/(2*σ1**2))
    ϕ2 = np.exp(-(x + 5)**2/(2*σ2**2))

    # Combined stress-energy tensor component
    C_tt = λ * (ϕ1**2 + ϕ2**2 + 2*ϕ1*ϕ2*np.exp(-λ*np.abs(σ1 - σ2)))
    return C_tt


# Parameters
x = np.linspace(-15, 15, 1000)
σ1, σ2 = 1.0, 1.2
λ_values = [0.5, 1.0, 2.0]

# Simulation
plt.figure(figsize=(12, 8))
for λ in λ_values:
    C_tt = multi_fpit_interaction(x, σ1, σ2, λ)
    plt.plot(x, C_tt, label=f'λ={λ}', lw=2)

plt.xlabel('Spatial Coordinate (x)', fontsize=14)
plt.ylabel('Constraint Tensor Component $C_{tt}$', fontsize=14)
plt.title('Multi-FPIT Causal Interference (Δσ = 0.2λ)', fontsize=16)
plt.legend()
plt.grid(True)
plt.savefig('multi_fpit_interference.pdf', dpi=300, bbox_inches='tight')
