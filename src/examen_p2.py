import numpy as np
from dataclasses import dataclass
from typing import Tuple, List, Dict
import os
from .utils.grapher import discrete_plotter

@dataclass
class SignalParams:
    f1: float = 8.0;  a1: float = 1.0
    f2: float = 20.0; a2: float = 0.5
    fn: float = 12.0; an: float = 0.4
    fs: float = 256.0
    duration: float = 6.0

def generate_signals(p: SignalParams) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    N = int(np.round(p.fs * p.duration))
    n = np.arange(N); t = n / p.fs
    x_clean = p.a1*np.sin(2*np.pi*p.f1*t) + p.a2*np.sin(2*np.pi*p.f2*t)
    x_noisy = x_clean + p.an*np.sin(2*np.pi*p.fn*t)
    return n, t, x_clean, x_noisy

def dft(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=complex); N = x.size
    n = np.arange(N); k = n.reshape((N,1))
    W = np.exp(-2j*np.pi*k*n/N)
    return W @ x

def spectrum_info(X: np.ndarray, fs: float):
    N = X.size; delta_f = fs / N
    kmax = N//2
    f_pos = np.arange(kmax+1) * delta_f
    mag = np.abs(X[:kmax+1]) / (N/2)
    return f_pos, mag, delta_f

def find_peaks(f: np.ndarray, mag: np.ndarray, rel_thresh: float = 0.05) -> List[Tuple[float,float]]:
    if mag.size < 3 or mag.max()==0: return []
    rel = mag / mag.max(); peaks=[]
    for i in range(1, len(mag)-1):
        if mag[i] > mag[i-1] and mag[i] > mag[i+1] and rel[i] >= rel_thresh:
            peaks.append((float(f[i]), float(rel[i])))
    return peaks

def plot_spectrum(f, mag, out_path, title="Espectro"):
    import matplotlib.pyplot as plt, os
    plt.figure(); plt.plot(f, mag); plt.title(title)
    plt.xlabel("f [Hz]"); plt.ylabel("|X(f)| (relativo)")
    plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout(); plt.savefig(out_path, dpi=150); plt.close()

def plot_overlay(f, mag1, mag2, labels, out_path, title="Comparación de espectros"):
    import matplotlib.pyplot as plt, os
    plt.figure()
    plt.plot(f, mag1, label=labels[0]); plt.plot(f, mag2, label=labels[1])
    plt.title(title); plt.xlabel("f [Hz]"); plt.ylabel("|X(f)| (relativo)")
    plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.6); plt.legend()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout(); plt.savefig(out_path, dpi=150); plt.close()

def run_examen_p2(p: SignalParams, outdir: str = "outputs", peak_threshold: float = 0.05) -> Dict:
    os.makedirs(outdir, exist_ok=True)
    n, t, x_clean, x_noisy = generate_signals(p)

    # Tiempo discreto: guarda PNGs
    discrete_plotter(n, x_clean, p.fs, os.path.join(outdir,"tiempo_discreto_limpia.png"), "Señal discreta (limpia)")
    discrete_plotter(n, x_noisy, p.fs, os.path.join(outdir,"tiempo_discreto_ruido.png"), f"Señal discreta con ruido (f_r={p.fn} Hz)")

    # Espectros
    Xc = dft(x_clean);  f,  mag_c, delta_f = spectrum_info(Xc, p.fs)
    Xn = dft(x_noisy); f2, mag_n, _        = spectrum_info(Xn, p.fs)
    plot_spectrum(f,  mag_c, os.path.join(outdir,"espectro_limpia.png"), "Espectro (limpia)")
    plot_spectrum(f2, mag_n, os.path.join(outdir,"espectro_ruido.png"),  "Espectro (con ruido)")
    plot_overlay(f, mag_c, mag_n, ["Limpia","Con ruido"], os.path.join(outdir,"espectro_comparacion.png"), "Comparación de espectros")

    peaks_clean = find_peaks(f,  mag_c, rel_thresh=peak_threshold)
    peaks_noisy = find_peaks(f2, mag_n, rel_thresh=peak_threshold)

    return {
        "N": int(p.fs * p.duration), "fs": p.fs, "delta_f": delta_f,
        "params": {"f1": p.f1, "a1": p.a1, "f2": p.f2, "a2": p.a2, "fn": p.fn, "an": p.an},
        "peaks_clean": [{"freq": fr, "rel_amp": ar} for fr, ar in peaks_clean],
        "peaks_noisy": [{"freq": fr, "rel_amp": ar} for fr, ar in peaks_noisy],
    }
