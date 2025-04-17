import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

plt.subplots_adjust(wspace=0.3)

# Panel 1: Quantum Stabilizer Code (Surface Code)
ax1.set_title("Quantum Error-Correcting Code\n(Stabilizer Checks)")
ax1.set_xlim(0, 4)
ax1.set_ylim(0, 4)
ax1.set_xticks([])
ax1.set_yticks([])

# Qubit grid (surface code)
for x in range(1, 4):
    for y in range(1, 4):
        ax1.plot(x, y, 'ko', markersize=8)  # Qubits
        if x < 3:
            ax1.plot([x, x+1], [y, y], 'b-', lw=2)  # X stabilizers
        if y < 3:
            ax1.plot([x, x], [y, y+1], 'r-', lw=2)  # Z stabilizers
ax1.text(2, 0.5, "Stabilizers Project\nOut Local Errors", ha='center')

# Panel 2: Spacetime Constraints
ax2.set_title(r"Constraint Tensor $C_{\mu\nu}$\nEnforcing Metric Rigidity")
ax2.set_xlim(0, 4)
ax2.set_ylim(0, 4)
ax2.set_xticks([])
ax2.set_yticks([])

# Spacetime manifold with FPIT
x = np.linspace(0, 4, 100)
y = 2 + 0.5 * np.sin(2 * np.pi * x / 4)
ax2.plot(x, y, 'k-', lw=3, label="Spacetime Metric")

# Perturbations and suppression
ax2.fill_between(x, y - 0.1, y + 0.1, color='red',
                 alpha=0.2, label="Perturbations")
ax2.fill_between(x[20:80], y[20:80] - 0.05, y[20:80] + 0.05,
                 color='green', alpha=0.3, label=r"$C_{\mu\nu}$ Stabilization")
ax2.legend(loc='lower right')

# Central analogy arrow
fig.text(0.5, 0.6, "Structural Analogy\n(Rigidity via Constraints)",
         ha='center', va='center', fontsize=12, color='purple')

plt.tight_layout()
plt.savefig("qecc_analogy.pdf", bbox_inches='tight')
