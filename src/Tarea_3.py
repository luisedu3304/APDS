import numpy as np
from src.utils.grapher import continuous_plotter, discrete_plotter

def compare_sine_signals(amplitude, frequency, phase):
    # Señal continua
    t = np.linspace(-1, 5, 1000)
    ref_cont = np.sin(2 * np.pi * 1 * t + 0)
    mod_cont = amplitude * np.sin(2 * np.pi * frequency * t + phase)

    # Graficar señales continuas una por una
    continuous_plotter(t, ref_cont, "Referencia: A=1, f=1Hz, ϕ=0", 'r', '--')
    continuous_plotter(t, mod_cont, f"Modificada: A={amplitude}, f={frequency}Hz, ϕ={phase}", 'b', '-')

    # Señal discreta
    Ts = 0.01
    n = np.arange(0, 600)
    t_discrete = n * Ts
    ref_disc = np.sin(2 * np.pi * 1 * t_discrete + 0)
    mod_disc = amplitude * np.sin(2 * np.pi * frequency * t_discrete + phase)

    # Graficar señales discretas una por una
    discrete_plotter(t_discrete, ref_disc, "Referencia: A=1, f=1Hz, ϕ=0", 'r', 'r--')
    discrete_plotter(t_discrete, mod_disc, f"Modificada: A={amplitude}, f={frequency}Hz, ϕ={phase}", 'b', 'b-')
