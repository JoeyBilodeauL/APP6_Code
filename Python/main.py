import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def A_2():
    fe : int = 20000
    N : int = 1024
    n : np.array = np.arange(N)
    x : np.array = np.sin(2 * np.pi * 400 * n / fe)
    X : np.array = np.fft.fft(x)
    X_mag_dB : np.array = 100 * np.log10(np.abs(X) * np.abs(X))

    plt.figure()
    plt.semilogx(n[:N//2] * fe / N, X_mag_dB[:N//2])
    plt.grid()
    plt.xlabel("Fréquence [Hz]")
    plt.ylabel("Amplitude [dB]")
    plt.title("Graphique de |X[k]|^2 du spectre d'un sinus d'entrée de 400 Hz")
    plt.show()



if __name__ == "__main__":
    A_2()