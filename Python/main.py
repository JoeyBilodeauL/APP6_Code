import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import From_Python_To_C_Array

def A_2():
    fe : int = 20000
    N : int = 1024
    n : np.array = np.arange(N)
    M : np.array = np.blackman(N)
    x : np.array = np.sin(2 * np.pi * 400 * n / fe)
    X : np.array = np.fft.fft(x)
    X_win : np.array = np.fft.fft(x * M)
    X_mag_dB : np.array = 100 * np.log10(np.abs(X) * np.abs(X))
    X_mag_dB_window : np.array = 100 * np.log10(np.abs(X_win) * np.abs(X_win))

    From_Python_To_C_Array.array_to_txt(np.blackman(768), 768, "Blackman" )

    plt.figure()
    plt.plot(n, X_mag_dB, label="Sans fenêtrage")
    plt.plot(n, X_mag_dB_window, label="Avec fenêtrage Blackman")
    plt.grid()
    plt.xlabel("Fréquence [k]")
    plt.ylabel("Amplitude [dB]")
    plt.title("Graphique de |X[k]|^2 du spectre d'un sinus d'entrée de 400 Hz")
    plt.legend()
    plt.show()



if __name__ == "__main__":
    A_2()