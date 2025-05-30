# 📊 Análisis y Visualización de Señales

Proyecto en Python para graficar diferentes tipos de señales en sus formas **continuas y discretas**, además de una señal senoidal con **frecuencia variable**, como parte de la materia de Procesamiento de Señales.

---

## 📁 Estructura del Proyecto

├── main.py # Punto de entrada para ejecutar tareas desde terminal
├── README.md # Este archivo de documentación
├── requirements.txt # Librerías necesarias para correr el proyecto
└── src/
├── Tarea_1.py # Señales: senoidal, exponencial, triangular y cuadrada
├── Tarea_2.py # Señal senoidal con frecuencia variable
└── utils/
└── grapher.py # Funciones para graficar señales continuas y discretas


---

## 🧠 Funcionalidades

### 🔹 Tarea 1 – Tipos de Señales

Incluye las siguientes señales, tanto en forma continua como discreta:

| Tipo de señal    | Notación continua                 | Notación discreta                    |
|------------------|-----------------------------------|--------------------------------------|
| Senoidal         | `x₁(t) = sin(2π·f·t)`              | `x₁[n] = sin(2π·f·n)`                |
| Exponencial      | `x₂(t) = e^(–2t)·u(t)`             | `x₂[n] = e^(–2·n·Ts)·u[n]`           |
| Triangular       | `x₃(t) = tri(t, f)`                | `x₃[n] = tri(n·Ts, f)`               |
| Cuadrada         | `x₄(t) = sq(t, f)`                 | `x₄[n] = sq(n·Ts, f)`                |

---

### 🔹 Tarea 2 – Señal Senoidal con Frecuencia Variable

Permite visualizar una señal senoidal continua con la frecuencia deseada por el usuario.

```python
x(t) = sin(2π·f·t)

