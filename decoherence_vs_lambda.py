"""
decoherence_simulation.py - Full Lindblad Dynamics Implementation
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

try:
    from qutip import (qeye, mesolve, basis, Options)
    QUTIP_INSTALLED = True
except ImportError:
    QUTIP_INSTALLED = False

# ========== PLOT STYLING ==========
plt.style.use('seaborn-v0_8-paper')
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'grid.alpha': 0.3
})

# ========== THEORETICAL MODEL ==========


def theoretical_decay(λ, λ0=1.0, P0=1.0):
    """Analytical solution for decoherence suppression"""
    return P0 * np.exp(-λ/λ0)

# ========== QUANTUM SIMULATION ==========


def lindblad_simulation(λ_values):
    """Reliable Lindblad simulation with QuTiP"""
    if not QUTIP_INSTALLED:
        raise ImportError("QuTiP required for Lindblad simulations")

    P_sim = []
    for λ in λ_values:
        try:
            # System definition
            H = 0 * qeye(2)
            L = np.sqrt(λ) * (basis(2, 0).proj() - basis(2, 1).proj())
            rho0 = basis(2, 0).proj()

            # Time evolution parameters
            tlist = np.linspace(0, 10, 100)

            result = mesolve(
                H=H,
                rho0=rho0,
                tlist=tlist,
                c_ops=[L],
                e_ops=[rho0],
                options=Options(store_states=True, nsteps=100000)
            )

            # Verify successful simulation
            if len(result.expect[0]) == 0:
                raise RuntimeError("Empty expectation values")

            P_sim.append(result.expect[0][-1])

        except Exception as e:
            print(f"Simulation failed at λ={λ:.2f}: {str(e)}")
            P_sim.append(np.nan)

    return np.array(P_sim)

# ========== DATA GENERATION ==========


def generate_data(λ_range=(0, 3), n_points=100):
    """Generate combined synthetic and Lindblad data"""
    λ = np.linspace(*λ_range, n_points)

    # Synthetic data with 5% noise
    np.random.seed(42)
    P_synth = theoretical_decay(λ) * (1 + 0.05*np.random.normal(size=n_points))

    # Lindblad simulation (if available)
    P_sim = lindblad_simulation(λ) if QUTIP_INSTALLED else None

    return λ, P_synth, P_sim

# ========== PLOTTING ==========


def create_figure(save_path='decoherence_vs_lambda.pdf'):
    """Main figure generation routine"""
    λ, P_synth, P_sim = generate_data()

    # Fit to theoretical model
    params, _ = curve_fit(theoretical_decay, λ, P_synth, p0=[1.0, 1.0])
    λ0_fit, P0_fit = params

    # Create figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8),
                                   gridspec_kw={'height_ratios': [3, 1]})

    # Top panel: Probability plot
    ax1.semilogy(λ, P_synth, 'ko', markersize=5, alpha=0.7,
                 label='Synthetic Data')
    if P_sim is not None:
        ax1.semilogy(λ, P_sim, 'b^', markersize=6, alpha=0.7,
                     label='Lindblad Simulation')

    theory_line = ax1.plot(λ, theoretical_decay(λ, λ0_fit, P0_fit),
                           'r-', lw=2,
                           label=rf'Theory: $P = e^{{-\lambda/{λ0_fit:.2f}}}$')

    ax1.axvline(1.0, color='gray', ls='--',
                label=r'Critical $\lambda_{\mathrm{crit}}$')
    ax1.set_ylabel(r'Branching Probability $P$')
    ax1.legend()
    ax1.grid(True, which='both', alpha=0.3)

    # Bottom panel: Residuals
    residuals = P_synth - theoretical_decay(λ, λ0_fit, P0_fit)
    ax2.plot(λ, residuals, 'ko', markersize=4, alpha=0.7)
    ax2.axhline(0, color='r', ls='-', lw=1)
    ax2.fill_between(λ, -0.1, 0.1, color='gray', alpha=0.2,
                     label=r'$\pm10\%$ Band')

    if P_sim is not None:
        res_sim = P_sim - theoretical_decay(λ, λ0_fit, P0_fit)
        ax2.plot(λ, res_sim, 'b^', markersize=4, alpha=0.7,
                 label='Lindblad Residuals')

    ax2.set_xlabel(r'Constraint Strength $\lambda$')
    ax2.set_ylabel('Residuals')
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(-0.15, 0.15)

    plt.tight_layout()
    plt.savefig(save_path, bbox_inches='tight')
    print(f"Figure saved to {save_path}")


if __name__ == "__main__":
    if not QUTIP_INSTALLED:
        print("Warning: QuTiP not installed - using synthetic data only")
    create_figure()
