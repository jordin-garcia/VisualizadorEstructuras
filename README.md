# Visualizador de Estructuras de Datos

Este programa permite visualizar gráficamente diferentes estructuras de datos y realizar operaciones sobre ellas.

## Estructuras soportadas
- Pilas
- Colas
- Listas simplemente enlazadas
- Listas circulares
- Listas doblemente enlazadas
- Árboles binarios
- Árboles binarios de búsqueda

## Características
- Soporte para diferentes tipos de datos (enteros, flotantes, booleanos, cadenas, objetos)
- Interfaz gráfica interactiva con PyQt5
- Visualización gráfica usando Graphviz
- Operaciones específicas para cada estructura

## Requisitos
- Python 3.6+
- PyQt5
- Graphviz (tanto el paquete Python como el software)

## Instalación

### 1. Instalación de dependencias de Python
```
pip install -r requirements.txt
```

### 2. Instalación de Graphviz

#### Windows
1. Descarga Graphviz desde https://graphviz.org/download/
2. Instala el software
3. Añade la carpeta bin del directorio de instalación de Graphviz a la variable de entorno PATH

#### macOS
```
brew install graphviz
```

#### Linux (Ubuntu/Debian)
```
sudo apt-get install graphviz
```

## Ejecución
```
python main.py
```

## Uso
1. Seleccione el tipo de estructura de datos que desea visualizar
2. Seleccione el tipo de datos que contendrá la estructura
3. Haga clic en "Crear Estructura"
4. Use los controles específicos para realizar operaciones sobre la estructura
5. Observe la visualización gráfica actualizada después de cada operación 