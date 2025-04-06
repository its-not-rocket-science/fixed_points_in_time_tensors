# anec_proof.py
import numpy as np
import matplotlib.pyplot as plt

# parameters from paper
phi0 = 1.0  # From {eq:phi_normalization} \phi_0 = (G/c^4)^{1/2}
sigma = 1.0  # Localization scale in light-years
lam = 1.5    # Constraint strength parameter


def phi(r):
    """Gaussian scalar field from Eq.(4)"""
    return phi0 * np.exp(-(r**2)/(2*sigma**2))


def dphidr(r):
    """Radial derivative of phi"""
    return -phi(r) * r / sigma**2


def exotic_stress_energy_tensor(r):
    """Energy density component from {eq:exotic_stress_energy}"""
    return -(lam/(8*np.pi)) * (dphidr(r)**2 - 0.5*(dphidr(r)**2 + phi(r)**2))


r = np.linspace(0, 5*sigma, 1000)
rho = exotic_stress_energy_tensor(r)
integral = np.cumsum(rho) * (r[1]-r[0])

plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(r/sigma, rho, 'r-', label=r'$\rho_{\rm exotic}(r)$')
plt.ylabel(r'$\rho\ [{\rm Planck\ units}]$', fontsize=12)
plt.title('ANEC Violation Proof: Actual Field Configuration', fontsize=14)
plt.axvline(1, color='k', linestyle='--', label='Throat Radius $b_0$')

plt.subplot(2, 1, 2)
plt.plot(r/sigma, integral, 'b-')
plt.xlabel(r'$r/\sigma$', fontsize=12)
plt.ylabel(r'$\int \rho\ dr$', fontsize=12)
plt.axhline(0, color='k', linestyle='--')
plt.grid(True)
plt.tight_layout()
plt.savefig('anec_proof.pdf', bbox_inches='tight')
