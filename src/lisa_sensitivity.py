import numpy as np
import matplotlib.pyplot as plt

# Configure LaTeX styling
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 14,
    "axes.titlesize": 16,
    "legend.fontsize": 12
})

def lisa_sensitivity(f):
    """LISA noise curve model from Robson+2019"""
    L = 2.5e9  # Arm length in meters
    f_0 = 19.09e-3  # Transfer frequency in Hz
    S_n = (10/3) * (4 * S_acc(f) + S_oms(f)) / (2*np.pi*f)**4 / L**2
    return np.sqrt(S_n) * 1e23  # Convert to dimensionless strain

def S_acc(f):
    """Acceleration noise PSD"""
    return 9e-30 * (1 + (0.4e-3/f)**2) * (1 + (f/8e-3)**4)

def S_oms(f):
    """Optical metrology noise PSD"""
    return 2.25e-22 * (1 + (2e-3/f)**4)

# Generate data
f = np.logspace(-4, -1, 300)  # 0.1 mHz to 100 mHz
lisa_curve = lisa_sensitivity(f)
fpit_strain = 1e-23 * (f/1e-3)**(-2.5)  # FPIT scaling law

# Plot
plt.figure(figsize=(10,6))
plt.loglog(f, lisa_curve, 'k-', lw=2, label='LISA Sensitivity (Robson+2019)')
plt.loglog(f, fpit_strain, 'r--', lw=2, label='FPIT Predicted Signal')
plt.xlabel('Frequency [Hz]', fontsize=14)
plt.ylabel(r'Characteristic Strain $(h/\sqrt{\rm Hz})$', fontsize=14)
plt.title('LISA Sensitivity vs FPIT Gravitational Wave Signals', fontsize=16)
plt.grid(True, which='both', alpha=0.4)
plt.legend()
plt.xlim(1e-4, 1e-1)
plt.ylim(1e-24, 1e-18)
plt.tight_layout()
plt.savefig('lisa_curve.pdf', bbox_inches='tight')