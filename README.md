Señales y Análisis de DAC en Python
Este repositorio contiene scripts para generar, comparar y analizar señales clásicas (senoidales, exponenciales, triangulares y cuadradas), tanto en tiempo continuo como discreto, además de un análisis de resolución de un DAC.

📂 Contenido
Archivo	Descripción	Función principal
signals.py	Señales clásicas continuas y discretas: senoidal, exponencial, triangular y cuadrada.	continuous_sine(), discrete_square() y más
user_sine_freq.py	Genera señal senoidal continua con frecuencia definida por el usuario.	understanding_freq(des_freq)
compare_sine.py	Compara señales senoidales continuas y discretas con amplitud, frecuencia y fase variables.	compare_sine_signals(amplitude, frequency, phase)
dac_analysis.py	Análisis de resolución y salida de un DAC dado el número de bits.	analyze_dac_resolution(bits)

🛠 Requisitos
Python 3.x

Librerías:

numpy

scipy

matplotlib (para las funciones gráficas personalizadas)

Módulo personalizado src.utils.grapher con funciones:

continuous_plotter

discrete_plotter

dac_plotter

🚀 Uso rápido
Generar señal senoidal con frecuencia personalizada
python
Copiar
Editar
from user_sine_freq import understanding_freq

understanding_freq(3)  # Genera y grafica señal senoidal de 3 Hz
Comparar señales senoidales (continua y discreta)
python
Copiar
Editar
from compare_sine import compare_sine_signals

compare_sine_signals(amplitude=2, frequency=1.5, phase=0.5)
Analizar resolución DAC
python
Copiar
Editar
from dac_analysis import analyze_dac_resolution

analyze_dac_resolution(8)  # Análisis para DAC de 8 bits
📈 Descripción detallada de los scripts
1. Señales clásicas continuas y discretas (signals.py)
Señales generadas:

Senoidal

Exponencial

Triangular

Cuadrada

Soporta tanto señales continuas como discretas.

Utiliza funciones de scipy.signal para señales triangulares y cuadradas.

Gráficas claras y diferenciadas para cada tipo de señal.

2. Señal senoidal continua con frecuencia variable (user_sine_freq.py)
Permite definir la frecuencia deseada.

Grafica señal senoidal con alta resolución en tiempo continuo.

Ideal para entender el efecto de la frecuencia sobre la señal.

3. Comparación de señales senoidales continuas y discretas (compare_sine.py)
Compara una señal base (amplitud=1, freq=1 Hz, fase=0) con una señal modificada.

Parámetros modificables: amplitud, frecuencia y fase.

Grafica ambas señales de forma continua y discreta para visualización directa.

4. Análisis y visualización de la resolución de un DAC (dac_analysis.py)
Calcula niveles de cuantización, tamaño del paso y resolución porcentual.

Grafica la salida analógica correspondiente a cada nivel digital.

Útil para comprender cómo el número de bits afecta la precisión del DAC.

