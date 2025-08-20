# Transformada de Fourier Discreta (DFT) — Examen 2

## Objetivo
Generar una **señal discreta** suma de senos y **agregar un tono ajeno** (ruido determinista) para analizar su espectro con una **DFT implementada por mí**, identificar picos y calcular la **resolución en frecuencia** \(\Delta f = f_s/N\).

## Señal de trabajo
Señal base (limpia):
\[
x[n] = a_1\sin\!\big(2\pi f_1 \tfrac{n}{f_s}\big) + a_2\sin\!\big(2\pi f_2 \tfrac{n}{f_s}\big)
\]
Ruido determinista (tono ajeno):
\[
r[n] = a_r\sin\!\big(2\pi f_r \tfrac{n}{f_s}\big)
\]
Señal con ruido: \(x_r[n]=x[n]+r[n]\)

**Parámetros por defecto**:  
\(f_s=256\ \text{Hz}\), duración \(6\ \text{s}\Rightarrow N=1536\) → \(\Delta f = \frac{f_s}{N}=0.166667\ \text{Hz}\).  
\(f_1=8\ \text{Hz},\ a_1=1.0;\quad f_2=20\ \text{Hz},\ a_2=0.5;\quad f_r=12\ \text{Hz},\ a_r=0.4.\)

**Picos esperados (limpia)**: ~8 Hz (1.0), ~20 Hz (0.5).  
**Picos esperados (con ruido)**: ~8 Hz (1.0), ~12 Hz (0.4), ~20 Hz (0.5).

## Estructura del repositorio
├── main.py
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   ├── examen_p2.py
│   └── utils/
│       └── grapher.py
└── outputs/            ← se genera al ejecutar (no se versiona)

Notas rápidas:
outputs/
*.png
*.pdf
