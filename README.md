# Python for Finance (UFM, 2025)

Este es el repositorio con los contenidos vistos en el curso de **Python for Finance** de la Universidad Franciso Marroquín (UFM) en la edición de septiembre de 2025.

## Requisitos

Para seguir el curso se necesita realizar la instalación de los siguientes programas:
* [Visual Studio Code](https://code.visualstudio.com)
* [Python 3.13](https://www.python.org)

### Windows

Se recomienda usar Python usando la Microsoft Store. Para ello, abrir Microsoft Store, buscar Python 3.13 e instalar. También se recomienda instalar Visual Studio Code desde Microsoft Store.

### Mac

Para usuarios de Mac se recomienda instalar el gestor de paquetes [Brew](https://brew.sh).

Una vez instalado:

```bash
brew install python
```

Y para Visual Studio Code:
```bash
brew install --cask visual-studio-code
```

### Extensiones

Además, se recomienda instalar las siguientes extensiones para Visual Studio Code:
* [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

### Enlaces de interés
* [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)


## Gestor de paquetes

En el curso se usará el gestor de paquetes [uv](https://docs.astral.sh/uv/).

### Instalación

Para su instalación se recomienda seguir la [guía de instalación recomendada](https://docs.astral.sh/uv/getting-started/installation/).

Para usuarios de Mac se recomienda instalar con el gestor de paquetes [Brew](https://brew.sh).

### Uso

Se recomienda usar los siguientes comandos:
* `uv init`: inicializar proyecto.
* `uv add <package>`: añadir paquete
* `uv remove <package>`: eliminiar paquete
* `uv sync`: sincronizar con la configuración en `pyproject.toml`

Una vista general de comandos puede ser consultado en [Features](https://docs.astral.sh/uv/getting-started/features/#the-pip-interface).

## Entregas

Las entregas consistirán en un fichero de tipo Jupyter Notebook, que llevará el nombre: `E[xx]_[apellido1]_[nombre].ipynb`, siendo `xx` el número de entrega, e.g. `E01_Perez_Juan.ipynb`.

### Entrega 1. Procesado de CSV

En esta entrega os familiarizaréis con la lectura de CSV y el procesado básico en Pandas. Para ello:
1. Descargad un set de datos en CSV que os interese (e.g. de la Reserva Federal, o de cualquier otra fuente)
2. Leedlo con `pd.read_csv`
3. Examinad qué hay dentro (`.head()`, `.describe()`...)
4. Haced una gráfica que os resulte interesante con los datos con `matplotlib`

### Entrega 2. Datos OCDE

En esta entrega tenéis que graficar agregados monetarios procedentes del portal de datos de la OECD. Para ello os dejo como referencia un notebook que os he preparado, y cuyas funciones podéis usar: https://github.com/MiguelPuntoEs/ufm-python-for-finance/blob/main/07%20OECD.ipynb
En esta entrega tenéis que graficar los agregados M1 (*narrow money*) y M3 (*broad money*) para tres países de vuestra elección. Os pido, en una misma gráfica para los tres países:
- Gráfica con M1
- Gráfica con M3
- Gráfica con M1 y M3
- Gráfica con el cambio absoluto anual de M1
- Gráfica con el cambio porcentual anual de M1
- Gráfica con el cambio absoluto con respecto a cinco años atrás de M3
- Gráfica con el cambio porcentual con respecto a cinco años atrás de M3

### Entrega 3. Regresión

En esta entrega deberéis plantear una regresión lineal. Para ello, pensad qué dos variables pueden tener cierta correlación, buscad los datos, y haced una regresión lineal con una única variable. Determinad el parámetro R cuadrado, explicad brevemente en qué consiste este parámetro y explicad el resultado obtenido.
Una vez hecho, plantead regresiones no lineales (e.g. con el cuadrado de la variables), o alternativamente una regresión con varias variables.
Para ello usad cualquier paquete que provea de estos cálculos, e.g. scikit-learn, statsmodels.

### Entrega 4. Clasificación

Carga un dataset que consideres interesante (e.g. uno de los que proporciona la libería scikit-learn) e implementa un modelo de clasificación a través de (1) un árbol de decisión, y (2) otro modelo de clasificación que consideres oportuno. Evalúa asimismo la calidad de la clasificación con las métricas que consideres; no olvides hacer separación training/test y normalizar los datos si el modelo así lo requiere.

### Entrega 5. Series temporales

Busca una serie temporal que muestre periodicidad y tendencia y descarga los datos en formato CSV.
1. Carga los datos usando la librería `darts`.
2. Grafica los datos.
3. Realiza un split entrenamiento/test.
4. Busca otras series temporales que puedan tener relación o causalidad con esta serie temporal, impórtalas y grafícalas.
5. Explora las [métricas de error](https://unit8co.github.io/darts/generated_api/darts.metrics.html) que ofrece darts.


Última edición: 22 de septiembre de 2025.