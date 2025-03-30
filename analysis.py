import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# =================================================================
# LaTeX Setup for arXiv Publication Quality
# =================================================================
plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'font.size': 12,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.format': 'pdf',
    'savefig.bbox': 'tight',
    'text.latex.preamble': r'\usepackage{amsmath,amssymb,physics}'
})

# =================================================================
# Figure 1: Geodesic Convergence and Metric Suppression
# =================================================================


def create_figure1():
    # -------------------------
    # Figure 1a: Geodesic Convergence
    # -------------------------
    fig1, (ax1a, ax1b) = plt.subplots(1, 2, figsize=(7.5, 3))
    fig1.suptitle(r'\textbf{Fixed Point Dynamics}', y=1.02)

    # Geodesic solutions
    def geodesic(y, t, lambda0):
        x, v = y
        return [v, -lambda0 * x * np.exp(-x**2)]

    t = np.linspace(0, 5, 100)
    colors = plt.colormaps['viridis'](np.linspace(0, 1, 6))
    for i, x0 in enumerate([-2, -1.5, -1, 1, 1.5, 2]):
        sol = odeint(geodesic, [x0, 0], t, args=(10,))
        ax1a.plot(t, sol[:, 0], c=colors[i], lw=1.5, alpha=0.8)

    ax1a.scatter([5], [0], c='r', s=50, marker='*',
                 label=r'$\mathcal{P}$')
    ax1a.set_title(r'(a) Geodesic Convergence')
    ax1a.set_xlabel(r'Proper Time $\tau$')
    ax1a.set_ylabel(r'Spatial Coordinate $x$')
    ax1a.legend(loc='upper right')

    # -------------------------
    # Figure 1b: Metric Suppression
    # -------------------------
    x = np.linspace(-3, 3, 100)
    t = np.linspace(-3, 3, 100)
    X, T = np.meshgrid(x, t)

    h_tt = 0.5 * np.exp(-(X**2 + T**2))
    h_constrained = h_tt * (1 - np.exp(-(X**2 + T**2)/0.5))

    im = ax1b.pcolormesh(X, T, h_constrained,
                         shading='gouraud',
                         cmap='viridis',
                         rasterized=True)  # For vector PDF inclusion
    fig1.colorbar(im, ax=ax1b, label=r'$h_{tt}$')
    ax1b.scatter(0, 0, c='r', s=50, marker='*',
                 label=r'$\mathcal{P}$')
    ax1b.set_title(r'(b) Metric Suppression')
    ax1b.set_xlabel(r'Spatial Coordinate $x$')
    ax1b.set_ylabel(r'Time Coordinate $t$')
    ax1b.legend(loc='upper right')

    plt.tight_layout()
    plt.savefig('figure1.pdf', dpi=300, bbox_inches='tight')

# =================================================================
# Figure 2: Exotic Matter and Wormhole Stability
# =================================================================


def create_figure2():
    fig2, (ax2a, ax2b) = plt.subplots(1, 2, figsize=(7.5, 3))
    fig2.suptitle(r'\textbf{Wormhole Dynamics}', y=1.02)

    # -------------------------
    # Figure 2a: Exotic Matter
    # -------------------------
    r = np.linspace(0.1, 5, 100)
    rho = -1/(8*np.pi) * (1/(r**2 + 1))

    ax2a.plot(r, rho, 'crimson', lw=2)
    ax2a.fill_between(r, rho, 0, color='crimson', alpha=0.2)
    ax2a.axhline(0, color='k', ls='--', lw=1)
    ax2a.set_title(r'(a) Exotic Matter Profile')
    ax2a.set_xlabel(r'Radial Coordinate $r$')
    ax2a.set_ylabel(r'$\rho_{\text{exotic}}$')

    # -------------------------
    # Figure 2b: Wormhole Throat
    # -------------------------
    b0 = 1.0
    r = np.linspace(b0+0.01, 5, 100)
    g_rr = 1/(1 - b0/r)

    ax2b.plot(r, g_rr, 'navy', lw=2)
    ax2b.axvline(b0, color='darkorange', ls='--', lw=2,
                 label=r'Throat $r = b_0$')
    ax2b.set_ylim(0, 10)
    ax2b.set_title(r'(b) Metric Component')
    ax2b.set_xlabel(r'Radial Coordinate $r$')
    ax2b.set_ylabel(r'$g_{rr}(r)$')
    ax2b.legend(loc='upper left')

    plt.tight_layout()
    plt.savefig('figure2.pdf', dpi=300, bbox_inches='tight')


# =================================================================
# Generate All Figures
# =================================================================
if __name__ == "__main__":
    create_figure1()
    create_figure2()
    # plt.show()
