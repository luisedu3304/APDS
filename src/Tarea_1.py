import numpy as np
from scipy import signal #Es para aplicar las señales tiangular y cuadrada 
from src.utils.grapher import continuous_plotter, discrete_plotter


# 1. Señal senoidal continua
def continuous_sine():
    frequency = 2
    amplitude = 1
    number_of_points = 10000
    time_initial = -1
    time_final = 5
    time = np.linspace(time_initial, time_final, number_of_points)
    x_t = amplitude * np.sin(2 * np.pi * frequency * time)

    continuous_plotter(
        time, x_t,
        'Continuous Sine wave Signal', 'x₁(t) = sin(2π·f·t)',
        'Time [s]',  'Amplitude')


# 2. Señal senoidal discreta
def discrete_sine():
    frequency = 2
    amplitude = 1
    fs = 20
    ts = 1 / fs
    samples = 100
    n = np.arange(samples)
    x_n = amplitude * np.sin(2 * np.pi * frequency * n * ts)

    discrete_plotter(
        n, x_n,
        'Discrete Sine wave Signal', 'x₁[n] = sin(2π·f·n)',
        'Sample index [n]', 'Amplitude')


# 3. Señal exponencial continua x₂(t) = e^(–2t)·u(t)
def continuous_exponential():
    number_of_points = 1000
    time = np.linspace(-1, 5, number_of_points)
    u = np.heaviside(time, 1)  # u(t)
    x_t = np.exp(-2 * time) * u

    continuous_plotter(
        time, x_t,
        'Continuous Exponential Signal', 'x₂(t) = e^(–2t)·u(t)',
        'Time [s]', 'Amplitude')


# 4. Señal exponencial discreta
def discrete_exponential():
    samples = 100
    ts = 0.05
    n = np.arange(-20, samples)
    t = n * ts
    u = np.heaviside(t, 1)
    x_n = np.exp(-2 * t) * u

    discrete_plotter(
        n, x_n,
        'Discrete Exponential Signal', 'x₂[n] = e^(–2·n·Ts)·u[n]',
        'Sample index [n]', 'Amplitude')


# 5. Señal triangular continua
def continuous_triangle():
    frequency = 2
    number_of_points = 1000
    time = np.linspace(0, 2, number_of_points)
    x_t = signal.sawtooth(2 * np.pi * frequency * time, 0.5)  # 0.5 → forma triangular

    continuous_plotter(
        time, x_t,
        'Continuous Triangular Signal', 'x₃(t) = tri(t, f)',
        'Time [s]', 'Amplitude')


# 6. Señal triangular discreta
def discrete_triangle():
    frequency = 2
    fs = 100
    ts = 1 / fs
    samples = 200
    n = np.arange(samples)
    t = n * ts
    x_n = signal.sawtooth(2 * np.pi * frequency * t, 0.5)

    discrete_plotter(
        n, x_n,
        'Discrete Triangular Signal', 'x₃[n] = tri(n·Ts, f)',
        'Sample index [n]', 'Amplitude')


# 7. Señal cuadrada continua
def continuous_square():
    frequency = 2
    number_of_points = 1000
    time = np.linspace(0, 2, number_of_points)
    x_t = signal.square(2 * np.pi * frequency * time)

    continuous_plotter(
        time, x_t,
        'Continuous Square Signal', 'x₄(t) = sq(t, f)',
        'Time [s]', 'Amplitude')


# 8. Señal cuadrada discreta
def discrete_square():
    frequency = 2
    fs = 100
    ts = 1 / fs
    samples = 200
    n = np.arange(samples)
    t = n * ts
    x_n = signal.square(2 * np.pi * frequency * t)

    discrete_plotter(
        n, x_n,
        'Discrete Square Signal', 'x₄[n] = sq(n·Ts, f)',
        'Sample index [n]', 'Amplitude')