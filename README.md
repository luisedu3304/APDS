📈 Señales y Análisis DAC en Python
Repositorio con scripts para generar, comparar y analizar señales en tiempo continuo y discreto, además de realizar análisis de resolución de un DAC (Convertidor Digital a Analógico).

Contenido
Descripción de los scripts

Requisitos

Instrucciones de uso

Funciones destacadas

Contribuciones

Licencia

Descripción de los scripts
1. signals.py
Genera y grafica señales clásicas:

Señales continuas y discretas:

Senoidal

Exponencial

Triangular

Cuadrada

Utiliza numpy, scipy.signal y funciones personalizadas para graficar.

2. user_sine_freq.py
Genera una señal senoidal continua con frecuencia definida por el usuario.

Parámetros configurables:

Frecuencia

Tiempo inicial y final

Número de puntos para la gráfica

3. compare_sine.py
Compara señales senoidales continuas y discretas con parámetros modificables:

Amplitud

Frecuencia

Fase

Grafica la señal de referencia y la modificada para análisis visual.

4. dac_analysis.py
Realiza análisis de resolución de un DAC:

Calcula niveles totales, tamaño de paso y resolución porcentual.

Grafica la salida analógica en función de la entrada digital.

Requisitos
Python 3.x

Librerías:

numpy

scipy

matplotlib (usado en funciones de graficación personalizadas)

Módulo personalizado src.utils.grapher que debe incluir:

continuous_plotter

discrete_plotter

dac_plotter

Instrucciones de uso
Clonar este repositorio.

Instalar dependencias:

bash
Copiar
Editar
pip install numpy scipy matplotlib
Ejecutar o importar las funciones en un script o consola Python.

Funciones destacadas
python
Copiar
Editar
# Generar señal senoidal con frecuencia personalizada
from user_sine_freq import understanding_freq
understanding_freq(3)

# Comparar señales senoidales
from compare_sine import compare_sine_signals
compare_sine_signals(amplitude=2, frequency=1.5, phase=0.5)

# Analizar resolución DAC para 8 bits
from dac_analysis import analyze_dac_resolution
analyze_dac_resolution(8)
Contribuciones
Contribuciones para mejorar la visualización, agregar nuevos tipos de señales o funciones son bienvenidas.
Por favor, abre un issue o un pull request.

Licencia
Este proyecto está bajo licencia MIT.

