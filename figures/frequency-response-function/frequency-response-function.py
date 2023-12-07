import numpy as np
import matplotlib.pyplot as plt

# System Parameters - Easily Modifiable
frequency = 100
damping_ratio = 0.1
mass = 1000.0
stiffness = 100000


def generate_sodf_frf(omega_n, zeta):
    # Frequency range for plotting, starting from zero
    freq_range = np.linspace(0, 2 * omega_n / (2 * np.pi), 500)
    omega = 2 * np.pi * freq_range

    # FRF calculation for SDOF
    H = 1 / (omega_n**2 - omega**2 + 2j * zeta * omega_n * omega)

    return freq_range, np.abs(H)

def plot_frf(omega_n, zeta):
    freq_range, H = generate_sodf_frf(omega_n, zeta)

    plt.figure(figsize=(12, 4.5))
    plt.rcParams.update({'font.size': 18})

    plt.plot(freq_range, H, color='blue', linewidth=4)

    plt.xlabel('Frequency [$rad \cdot s^{-1}$]')
    plt.ylabel('Amplitude [-]')
    plt.title('Frequency Response Function of an SDOF System')
    plt.ylim(0,0.06)
    plt.xlim(0,3)

    plt.grid(True)
    plt.tight_layout()
    plt.savefig('frequency-response-function.png', bbox_inches='tight')
    plt.show()

# Convert frequency to rad/s and scale
omega_n = np.sqrt(stiffness / mass)

# Example usage with modifiable parameters
plot_frf(omega_n, damping_ratio)
