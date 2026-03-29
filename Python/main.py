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
    x : np.array = np.sin(2 * np.pi * 1000 * n / fe)
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
    plt.plot(n[256:], np.real(y)[256:])
    plt.show()

def filtre_FIR():
    fe : int = 20000
    H_LENGTH : int = 256
    N : int = 1024
    n = np.arange(N)
    fc_h7 : int = 500
    fc_h6 = [500, 1500]
    fc_h5 = [1500, 2500]
    fc_h4 = [2500, 4500]
    fc_h3 = 4490

    H7 : np.array = get_filter_transfer_function(N, H_LENGTH, fc_h7, "lowpass", "blackman", fe)
    H6 : np.array = get_filter_transfer_function(N, H_LENGTH, fc_h6, "bandpass", "blackman", fe)
    H5 : np.array = get_filter_transfer_function(N, H_LENGTH, fc_h5, "bandpass", "blackman", fe)
    H4 : np.array = get_filter_transfer_function(N, H_LENGTH, fc_h4, "bandpass", "blackman", fe)
    H3 : np.array = get_filter_transfer_function(N, H_LENGTH - 1, fc_h3, "highpass", "blackman", fe)

    From_Python_To_C_Array.array_to_txt(H7, N, "H7")
    From_Python_To_C_Array.array_to_txt(H6, N, "H6")
    From_Python_To_C_Array.array_to_txt(H5, N, "H5")
    From_Python_To_C_Array.array_to_txt(H4, N, "H4")
    From_Python_To_C_Array.array_to_txt(H3, N, "H3")

    h_tot : np.array = (signal.firwin(H_LENGTH, fc_h7, pass_zero="lowpass", window="blackman", fs=fe)[1:] +
                        signal.firwin(H_LENGTH, fc_h6, pass_zero="bandpass", window="blackman", fs=fe)[1:] +
                        signal.firwin(H_LENGTH, fc_h5, pass_zero="bandpass", window="blackman", fs=fe)[1:] +
                        signal.firwin(H_LENGTH, fc_h4, pass_zero="bandpass", window="blackman", fs=fe)[1:] +
                        signal.firwin(H_LENGTH - 1, fc_h3, pass_zero="highpass", window="blackman", fs=fe)
                        )
    H_tot : np.array = np.fft.fft(h_tot, n=N)
    H_tot_mag_dB : np.array = 20 * np.log10(np.abs(H_tot))


    plt.figure()

    plt.subplot(2,1,1)
    plt.plot(n * fe / N, 100 * np.log10(np.abs(H7) + 1), label=f"H7: lowpass (fc = {fc_h7} Hz)")
    plt.plot(n * fe / N, 100 * np.log10(np.abs(H6) + 1), label=f"H6: bandpass (fc = {(fc_h6[0] + fc_h6[1]) / 2} Hz)")
    plt.plot(n * fe / N, 100 * np.log10(np.abs(H5) + 1), label=f"H5: bandpass (fc = {(fc_h5[0] + fc_h5[1]) / 2} Hz)")
    plt.plot(n * fe / N, 100 * np.log10(np.abs(H4) + 1), label=f"H4: bandpass (fc = {(fc_h4[0] + fc_h4[1]) / 2} Hz)")
    plt.plot(n * fe / N, 100 * np.log10(np.abs(H3) + 1), label=f"H3: highpass (fc = {fc_h3} Hz)")
    plt.grid()
    plt.title("Fonction de transfert H[f]")
    #plt.xlabel("index [k]")
    plt.ylabel("Gain [dB]")
    plt.legend()

    plt.subplot(2,1,2)
    plt.semilogx(n[:N // 2] * fe / N, H_tot_mag_dB[:N // 2])
    plt.grid()
    plt.title("Somme des fonctions de transferts : H3 + H4 + H5 + H6 + H7")
    plt.xlabel("index [k]")
    plt.ylabel("Gain [dB]")
    plt.ylim(-50, 5)
    plt.show()

def filtre_IIR():
    print("bonjour")

def get_filter_transfer_function(N : int, numtaps : int, cutoff , type : str, window : str, fe : int):
    h_fir : np.array = signal.firwin(numtaps=numtaps, cutoff=cutoff, pass_zero=f"{type}", window=f"{window}", fs=fe)
    H_fir : np.array = np.fft.fft(h_fir, n=N)
    return H_fir

if __name__ == "__main__":
    filtre_FIR()