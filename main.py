#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Visualizador de Estructuras de Datos
-----------------------------------

Aplicación para visualizar gráficamente el funcionamiento de diversas
estructuras de datos y sus operaciones.

Este es el punto de entrada principal del programa.

Autor: [Tu Nombre]
Versión: 1.0
"""

import sys
from PyQt5.QtWidgets import QApplication
from gui import MainWindow

def main():
    """
    Función principal que inicia la aplicación.
    """
    # Crear la aplicación PyQt
    app = QApplication(sys.argv)
    
    # Crear y mostrar la ventana principal
    window = MainWindow()
    window.show()
    
    # Ejecutar el bucle de eventos
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 