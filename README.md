Descripción general
Este repositorio contiene cuatro scripts de Python para generar, analizar y graficar diferentes tipos de señales y funciones relacionadas con procesamiento de señales y electrónica digital. Se utilizan funciones personalizadas para graficar señales continuas y discretas, así como para analizar la resolución de un DAC (Convertidor Digital a Analógico).

Contenido
1. Señales clásicas continuas y discretas
Archivo: signals.py (o nombre similar)

Genera señales senoidales, exponenciales, triangulares y cuadradas en forma continua y discreta.

Utiliza numpy para cálculos numéricos y scipy.signal para señales especiales (triangular, cuadrada).

Usa funciones personalizadas continuous_plotter y discrete_plotter para graficar las señales.

Funciones principales:

continuous_sine()

discrete_sine()

continuous_exponential()

discrete_exponential()

continuous_triangle()

discrete_triangle()

continuous_square()

discrete_square()

2. Generación de señal senoidal continua con frecuencia definida por el usuario
Archivo: user_sine_freq.py (o nombre similar)

Permite generar y graficar una señal senoidal continua con una frecuencia definida por el usuario.

Parámetros ajustables: frecuencia, tiempo inicial y final, número de puntos para suavidad de la gráfica.

Función principal:

understanding_freq(des_freq)

3. Comparación entre señales senoidales continuas y discretas con parámetros variables
Archivo: compare_sine.py (o nombre similar)

Compara señales senoidales de referencia (amplitud 1, frecuencia 1 Hz, fase 0) con señales modificadas que pueden cambiar amplitud, frecuencia y fase.

Grafica ambas señales tanto en forma continua como discreta usando funciones personalizadas.

Función principal:

compare_sine_signals(amplitude, frequency, phase)

4. Análisis de resolución de un DAC
Archivo: dac_analysis.py (o nombre similar)

Analiza la resolución de un DAC dado un número de bits de entrada.

Calcula niveles totales, tamaño del paso y resolución porcentual.

Genera y grafica la salida analógica correspondiente a las entradas digitales.

Usa función personalizada dac_plotter para la gráfica.

Función principal:

analyze_dac_resolution(bits)

Requisitos
Python 3.x

Librerías:

numpy

scipy

matplotlib (asumido para las funciones de graficación personalizadas)

Módulo personalizado src.utils.grapher con las funciones:

continuous_plotter

discrete_plotter

dac_plotter

Cómo usar
Clonar el repositorio.

Asegurarse de tener instaladas las librerías necesarias.

Ejecutar cada script o importar las funciones para generar las señales y gráficos deseados.

Ejemplo de ejecución para generar señal senoidal continua con frecuencia 3 Hz:

python
Copiar
Editar
from user_sine_freq import understanding_freq
understanding_freq(3)
Ejemplo para analizar resolución DAC de 8 bits:

python
Copiar
Editar
from dac_analysis import analyze_dac_resolution
analyze_dac_resolution(8)
