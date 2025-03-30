import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 12,
    "axes.labelsize": 14,
    "axes.titlesize": 16,
    "legend.fontsize": 12,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "figure.dpi": 300,
    "savefig.bbox": 'tight',
    "savefig.pad_inches": 0.1
})

# Set up parameters
fs = 100000  # Sampling frequency (Hz)
t = np.linspace(0, 0.02, int(fs*0.02))  # 20ms time window

# Generate FPIT burst waveform (decaying sinusoid)
f_fpit = 200  # Frequency (Hz)
decay_time = 0.01  # 10ms decay
fpit_wave = np.sin(2*np.pi*f_fpit*t) * np.exp(-t/decay_time)

# Generate BBH merger chirp waveform
f0 = 50  # Initial frequency (Hz)
f1 = 300  # Final frequency (Hz)
bbh_wave = chirp(t, f0=f0, f1=f1, t1=0.02, method='hyperbolic') * (1 + t*50)

# Normalize waveforms
fpit_wave /= np.max(np.abs(fpit_wave))
bbh_wave /= np.max(np.abs(bbh_wave))

# Create plot
plt.figure(figsize=(10, 6))

# Plot waveforms
plt.plot(t*1000, fpit_wave, 'r', lw=2, label='FPIT Burst')
plt.plot(t*1000, bbh_wave, 'b--', lw=2, label='BBH Merger')

# Formatting
plt.xlabel('Time (ms)', fontsize=12)
plt.ylabel('Normalized Strain', fontsize=12)
plt.title('Gravitational Waveform Comparison', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.xlim(0, 20)
plt.ylim(-1.1, 1.1)

# Add frequency labels
plt.annotate('Quasi-monochromatic\n~200 Hz',
             xy=(5, 0.8), xycoords='data',
             fontsize=10, color='r', ha='center')

plt.annotate('Chirp: 50-300 Hz',
             xy=(15, -0.8), xycoords='data',
             fontsize=10, color='b', ha='center')

plt.tight_layout()
plt.savefig('gw_waveform.pdf', dpi=300, bbox_inches='tight')
# plt.show()
