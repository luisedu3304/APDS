import os
import matplotlib.pyplot as plt

def discrete_plotter(n, x, fs, out_path, title="Señal discreta"):
    t = n / fs
    plt.figure()
    try:
        plt.stem(t, x, use_line_collection=True)
    except TypeError:
        plt.stem(t, x)
    plt.title(title)
    plt.xlabel("t = n / f_s [s]")
    plt.ylabel("x[n]")
    plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()

def continuous_plotter(t, x, out_path, title="Señal continua"):
    plt.figure()
    plt.plot(t, x)
    plt.title(title)
    plt.xlabel("t [s]")
    plt.ylabel("x(t)")
    plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
