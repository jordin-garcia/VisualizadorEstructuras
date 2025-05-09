from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, 
    QPushButton, QLabel, QLineEdit, QFormLayout,
    QTextEdit, QScrollArea, QMessageBox
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class BasePanel(QWidget):
    """
    Panel base para todas las estructuras de datos.
    
    Esta clase proporciona la estructura común y funcionalidades
    compartidas entre todos los paneles de visualización.
    """
    
    def __init__(self):
        super().__init__()
        
        # Inicializar estructura
        self.structure = None
        
        # Configurar layout principal
        self.main_layout = QVBoxLayout(self)
        
        # Sección de información
        self.info_box = QGroupBox("Información de la Estructura")
        info_layout = QFormLayout(self.info_box)
        
        # Etiquetas de información
        self.type_label = QLabel("Tipo: -")
        self.size_label = QLabel("Tamaño: 0")
        self.data_type_label = QLabel("Tipo de Dato: -")
        self.extra_info_label = QLabel("")
        
        # Añadir etiquetas al layout
        info_layout.addRow(self.type_label)
        info_layout.addRow(self.size_label)
        info_layout.addRow(self.data_type_label)
        info_layout.addRow(self.extra_info_label)
        
        # Añadir sección de información al layout principal
        self.main_layout.addWidget(self.info_box)
        
        # Sección central: Visualización y operaciones
        center_layout = QHBoxLayout()
        
        # Panel de operaciones (izquierda)
        operations_box = QGroupBox("Operaciones")
        self.operations_layout = QVBoxLayout(operations_box)
        
        # Aquí cada subclase añadirá sus controles específicos
        
        center_layout.addWidget(operations_box, 1)
        
        # Panel de visualización (derecha)
        vis_box = QGroupBox("Visualización")
        vis_layout = QVBoxLayout(vis_box)
        
        # Área de visualización
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        self.visualization_widget = QLabel("Estructura no creada")
        self.visualization_widget.setAlignment(Qt.AlignCenter)
        scroll_area.setWidget(self.visualization_widget)
        
        vis_layout.addWidget(scroll_area)
        
        center_layout.addWidget(vis_box, 3)
        
        # Añadir sección central al layout principal
        self.main_layout.addLayout(center_layout, 1)
    
    def create_structure(self, data_type):
        """
        Crea la estructura de datos (debe ser implementado por las subclases).
        
        Args:
            data_type: Tipo de datos para la estructura
        """
        raise NotImplementedError("Las subclases deben implementar este método")
    
    def update_info(self):
        """
        Actualiza la información mostrada en el panel.
        """
        if self.structure:
            info = self.structure.get_info()
            self.type_label.setText(f"Tipo: {info['tipo']}")
            self.size_label.setText(f"Tamaño: {info['tamaño']}")
            self.data_type_label.setText(f"Tipo de Dato: {info['tipo_dato']}")
            
            # Actualizar información extra específica de cada estructura
            extra_info = []
            for key, value in info.items():
                if key not in ["tipo", "tamaño", "tipo_dato"]:
                    extra_info.append(f"{key}: {value}")
            
            self.extra_info_label.setText("\n".join(extra_info))
    
    def update_visualization(self):
        """
        Actualiza la visualización de la estructura (debe ser implementado por las subclases).
        """
        raise NotImplementedError("Las subclases deben implementar este método")
    
    def show_message(self, title, message):
        """
        Muestra un mensaje al usuario.
        
        Args:
            title: Título del mensaje
            message: Contenido del mensaje
        """
        QMessageBox.information(self, title, message)
    
    def show_error(self, title, message):
        """
        Muestra un mensaje de error al usuario.
        
        Args:
            title: Título del mensaje
            message: Contenido del mensaje
        """
        QMessageBox.critical(self, title, message) 