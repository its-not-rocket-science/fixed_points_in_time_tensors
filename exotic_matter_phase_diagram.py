import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "text.latex.preamble": r"\usepackage{amsmath}"
})

# Different potential functions
potentials = {
    'Gaussian': lambda ϕ, σ: np.exp(-ϕ**2/(2*σ**2)),
    'Quartic': lambda ϕ, σ: (ϕ**4)/(σ**4) - (ϕ**2)/(σ**2),
    'Hyperbolic': lambda ϕ, σ: np.cosh(ϕ/σ) - 1
}

# Stress-energy component calculation


def T_exotic(ϕ, V, dV, λ):
    return -λ * (0.5*(dV(ϕ))**2 - V(ϕ))


# Parameter space
ϕ = np.linspace(-3, 3, 500)
λ_range = np.logspace(-1, 2, 100)
σ = 1.0

# Phase diagram calculation
plt.figure(figsize=(14, 10))
for name, V_func in potentials.items():
    def V(ϕ): return V_func(ϕ, σ)
    def dV(ϕ): return np.gradient(V(ϕ), ϕ)
    T_values = [T_exotic(ϕ, V, dV, λ) for λ in λ_range]

    plt.contourf(ϕ, λ_range, T_values, levels=50, cmap='viridis')
    plt.colorbar(label=r'$T_{\mu\nu}^{\text{(exotic)}}$')
    plt.yscale('log')
    plt.xlabel('Field Value (ϕ)', fontsize=14)
    plt.ylabel('Constraint Strength (λ)', fontsize=14)
    plt.title(f'Exotic Matter Phase Diagram: {name} Potential', fontsize=16)
    plt.savefig(
        f'exotic_matter_phase_diagram_{name.lower()}.pdf', dpi=300,  bbox_inches='tight')
    plt.clf()
