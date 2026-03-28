import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import From_Python_To_C_Array

def A_2():
    fe : int = 20000
    N : int = 1024
    n : np.array = np.arange(N)
    M : np.array = np.blackman(N)
    x : np.array = np.sin(2 * np.pi * 440 * n / fe)
    X : np.array = np.fft.fft(x)
    X_win : np.array = np.fft.fft(x * M)
    X_mag_dB : np.array = 100 * np.log10(np.abs(X) * np.abs(X))
    k_max = np.argmax(X_mag_dB[:N//2])
    X_mag_dB_window : np.array = 100 * np.log10(np.abs(X_win) * np.abs(X_win))

    plt.figure()
    plt.plot(n, X_mag_dB, label="Sans fenêtrage")
    plt.plot(n, X_mag_dB_window, label="Avec fenêtrage Blackman")
    #plt.axvline(x=k_max, color='red', linestyle='--', label=f'k = {k_max}')
    plt.grid()
    plt.xlabel("Fréquence [k]")
    plt.ylabel("Puissance [dB]")
    plt.title("Graphique de |X[k]|^2 du spectre d'un sinus d'entrée de 440 Hz")
    plt.legend()
    plt.show()

def B_1():
    fe : int = 20000
    N : int = 1024
    n : np.array = np.arange(N)
    M : np.array = np.blackman(N)
    x : np.array = np.sin(2 * np.pi * 400 * n / fe)
    h : np.array = signal.firwin(256,500, window='blackman', fs=fe)
    H : np.array = np.fft.fft(h, n=N)
    X : np.array = np.fft.fft(x)
    X_mag_dB : np.array = 100 * np.log10(np.abs(X) * np.abs(X))
    Y : np.array = X * H
    Y_mag_dB : np.array = 100 * np.log10(np.abs(Y) * np.abs(Y) + 1)
    y : np.array = np.fft.ifft(Y)


    plt.figure()
    plt.grid()
    plt.xlabel("Fréquence [k]")
    #plt.ylabel("Puissance [dB]")
    #plt.title("Graphique de la puissance du spectre d'un sinus de 400 Hz de grandeur 4N")
    #plt.plot(n, X_mag_dB)
    plt.ylabel("Puissance [dB]")
    plt.title("Graphique de la puissance du spectre de Y[k]")
    plt.plot(n, Y_mag_dB)
    plt.show()


if __name__ == "__main__":
    B_1()