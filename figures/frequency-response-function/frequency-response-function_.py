import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

m1 = 1
c1 = 0.7
k1 = 4

m2 = m1
c2 = c1 * 0.5
k2 = k1 * 1.8

def generate_sodf_frf(m, c, k, omega_n):
    # Frequency range for plotting, starting from zero
    freq_range = np.linspace(0, 2.5 * omega_n, 500)
    omega = freq_range

    # FRF calculation for SDOF
    H = 1 / (k - m * omega ** 2 + 1j * omega * c)

    # Calculate magnitude and phase
    magnitude = np.abs(H)
    phase = np.angle(H)

    return freq_range, magnitude, phase

def plot_frf(m1, c1, k1, m2, c2, k2):
    omega_n_max = max(np.sqrt(k1/m1), np.sqrt(k2/m2))
    freq_range, magnitude, phase = generate_sodf_frf(m1, c1, k1, omega_n_max)
    _, magnitude_mod, phase_mod = generate_sodf_frf(m2, c2, k2, omega_n_max)

    zeta_1 = c1 / (2 * np.sqrt(k1 * m1))
    zeta_2 = c2 / (2 * np.sqrt(k2 * m2))

    omega_r_1 = np.sqrt(k1/m1) * np.sqrt(1 - 2 * zeta_1 ** 2)
    omega_r_2 = np.sqrt(k2/m2) * np.sqrt(1 - 2 * zeta_2 ** 2)

    plt.figure(figsize=(12, 9))
    plt.rcParams.update({'font.size': 18})

    # Plot magnitude
    plt.subplot(2, 1, 1)
    plt.plot(freq_range, magnitude, color='blue', linewidth=3.5,
             label=f'm={m1:.1f}, c={c1:.1f}, k={k1:.1f} $\Rightarrow$ $\\xi_r$={omega_r_1:.1f}, $\\zeta$={zeta_1:.1f}')
    plt.plot(freq_range, magnitude_mod, color='red', linewidth=3.5,
             label=f'm={m2:.1f}, c={c2:.1f}, k={k2:.1f} $\Rightarrow$ $\\xi_r$={omega_r_2:.1f}, $\\zeta$={zeta_2:.1f}')
    plt.xlabel('Angular Frequency, $\\xi$ [$rad \cdot s^{-1}$]')
    plt.ylabel('Abs(H($\\xi$)) [$m \cdot s^{-2} \cdot N^{-1}$]')
    plt.title('Magnitude of Frequency Response Function of an SDOF System')
    plt.ylim(0, 1.8)
    plt.xlim(0, 5)
    plt.legend()
    plt.grid(True)

    # Plot phase
    plt.subplot(2, 1, 2)
    plt.plot(freq_range, phase, color='blue', linewidth=3.5,
             label=f'm={m1:.1f}, c={c1:.1f}, k={k1:.1f} $\Rightarrow$ $\\xi_r$={omega_r_1:.1f}, $\zeta$={zeta_1:.1f}')
    plt.plot(freq_range, phase_mod, color='red', linewidth=3.5,
             label=f'm={m2:.1f}, c={c2:.1f}, k={k2:.1f} $\Rightarrow$ $\\xi_r$={omega_r_2:.1f}, $\zeta$={zeta_2:.1f}')

    plt.xlabel('Angular Frequency, $\\xi$ [$rad \cdot s^{-1}$]')
    plt.ylabel('Phase(H($\\xi$)) [rad]')
    plt.title('Phase of Frequency Response Function of an SDOF System')
    plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f'))
    plt.ylim(-3, 1.2)
    plt.xlim(0, 5)
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('frequency-response-function_.png', bbox_inches='tight')
    plt.show()

# Example usage with modifiable parameters
plot_frf(m1, c1, k1, m2, c2, k2)
