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