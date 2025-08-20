import numpy as np
from dataclasses import dataclass
from typing import Tuple, List
import os
from .utils.grapher import continuous_plotter, discrete_plotter

@dataclass
class SignalParams:
    fm: float = 0.5
    fc: float = 8.0
    m: float = 0.5
    fs: float = 256.0
    duration: float = 4.0

def generate_signal(p: SignalParams) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    N = int(np.round(p.fs * p.duration))
    n = np.arange(N)
    t = n / p.fs
    x = (1 + p.m * np.cos(2*np.pi*p.fm*t)) * np.sin(2*np.pi*p.fc*t)
    return t, n, x

def dft(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=complex)
    N = x.size
    n = np.arange(N)
    k = n.reshape((N, 1))
    W = np.exp(-2j * np.pi * k * n / N)
    return W @ x

def spectrum_info(X: np.ndarray, fs: float):
    N = X.size
    delta_f = fs / N
    kmax = N//2
    f_pos = np.arange(kmax + 1) * delta_f
    mag = np.abs(X[:kmax+1]) / (N/2)
    return f_pos, mag, delta_f

def find_peaks(f: np.ndarray, mag: np.ndarray, rel_thresh: float = 0.05):
    if mag.size < 3:
        return []
    rel = mag / (mag.max() if mag.max() > 0 else 1.0)
    peaks = []
    for i in range(1, len(mag)-1):
        if mag[i] > mag[i-1] and mag[i] > mag[i+1] and rel[i] >= rel_thresh:
            peaks.append((f[i], rel[i]))
    return peaks

def run_examen_p1(p: SignalParams, outdir: str = "Transformada de Fourier Discreta", peak_threshold: float = 0.05):
    os.makedirs(outdir, exist_ok=True)
    t, n, x = generate_signal(p)

    # 👇 Corrección: se pasa el título como 4º argumento posicional
    continuous_plotter(t, x, os.path.join(outdir, "Transformada de Fourier Discreta"), "x(t) continua")
    discrete_plotter(n, x, p.fs, os.path.join(outdir, "Transformada de Fourier Discreta.png"), "x[n] discreta")

    X = dft(x)
    f, mag, delta_f = spectrum_info(X, p.fs)

    import matplotlib.pyplot as plt
    plt.figure()
    plt.plot(f, mag)
    plt.title("Espectro de magnitud")
    plt.xlabel("f [Hz]")
    plt.ylabel("|X(f)|")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "espectro_mag.png"), dpi=150)
    plt.close()

    peaks = find_peaks(f, mag, rel_thresh=peak_threshold)
    return {
        "N": int(p.fs * p.duration),
        "fs": p.fs,
        "delta_f": delta_f,
        "peaks": [{"freq": float(fr), "rel_amp": float(ra)} for fr, ra in peaks]
    }
