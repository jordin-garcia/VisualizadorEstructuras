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