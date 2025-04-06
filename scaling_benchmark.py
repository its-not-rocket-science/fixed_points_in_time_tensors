import numpy as np
import matplotlib.pyplot as plt

# Theoretical scaling law: O(N^2 log N)


def theoretical_scaling(N, a=1e-6):
    return a * (N**2) * np.log(N)


# Synthetic data - replace with actual timing results
grid_sizes = np.array([32, 64, 128, 256])
runtimes = theoretical_scaling(
    grid_sizes) * np.random.uniform(0.9, 1.1, size=len(grid_sizes))

plt.figure(figsize=(8, 6))
plt.loglog(grid_sizes, theoretical_scaling(grid_sizes),
           'r--', label='Theoretical O(N² log N)')
plt.loglog(grid_sizes, runtimes, 'bo-', label='Actual Runtimes')
plt.xlabel('Grid Size (N)', fontsize=12)
plt.ylabel('Runtime (seconds)', fontsize=12)
plt.title('Weak Scaling Benchmark', fontsize=14)
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.savefig('scaling_benchmark.pdf', bbox_inches='tight')
plt.close()
