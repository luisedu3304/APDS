# Transformada de Fourier Discreta (DFT) — `examen_p1`

## Objetivo
Aplicar la **Transformada de Fourier Discreta (DFT)** a señales muestreadas; identificar picos espectrales, **estimar frecuencias y amplitudes relativas**; y calcular/usar la **resolución en frecuencia** \(\Delta f = f_s/N\).

## Señal de trabajo
Se analiza la señal:
\[
x(t) = \big[1 + m\cos(2\pi f_m t)\big]\sin(2\pi f_c t)
\]
Parámetros por defecto: `fm = 0.5 Hz`, `fc = 8 Hz`, `m = 0.5`.

- **Picos esperados** (AM de una sola tono): \(f_c \pm f_m\) y \(f_c\).
  - Para los valores por defecto: **7.5 Hz**, **8.0 Hz**, **8.5 Hz**.
  - Amplitudes **relativas** aproximadas: **0.25**, **1.00**, **0.25** (con la normalización usada).

## Estructura del repositorio
