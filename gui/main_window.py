from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QComboBox, QPushButton, QLabel, QStackedWidget, QGroupBox
)
from PyQt5.QtCore import Qt

from gui.stack_panel import StackPanel
from gui.queue_panel import QueuePanel
from gui.linked_list_panel import LinkedListPanel
from gui.circular_list_panel import CircularListPanel
from gui.doubly_linked_list_panel import DoublyLinkedListPanel
from gui.binary_tree_panel import BinaryTreePanel
from gui.binary_search_tree_panel import BinarySearchTreePanel

from utils.data_types import DataType

class MainWindow(QMainWindow):
    """
    Ventana principal de la aplicación.
    """
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualizador de Estructuras de Datos")
        self.setMinimumSize(1000, 700)
        
        # Configurar widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QVBoxLayout(central_widget)
        
        # Sección superior: Selección de estructura y tipo de dato
        top_section = QGroupBox("Configuración")
        top_layout = QHBoxLayout(top_section)
        
        # Selector de estructura de datos
        structure_layout = QVBoxLayout()
        structure_label = QLabel("Seleccione una estructura de datos:")
        self.structure_combo = QComboBox()
        self.structure_combo.addItems([
            "Pila (Stack)",
            "Cola (Queue)",
            "Lista Enlazada Simple",
            "Lista Circular",
            "Lista Doblemente Enlazada",
            "Árbol Binario",
            "Árbol Binario de Búsqueda"
        ])
        structure_layout.addWidget(structure_label)
        structure_layout.addWidget(self.structure_combo)
        top_layout.addLayout(structure_layout)
        
        # Selector de tipo de dato
        data_type_layout = QVBoxLayout()
        data_type_label = QLabel("Seleccione el tipo de dato:")
        self.data_type_combo = QComboBox()
        self.data_type_combo.addItems([
            "Entero",
            "Flotante",
            "Booleano",
            "Cadena",
            "Objeto"
        ])
        data_type_layout.addWidget(data_type_label)
        data_type_layout.addWidget(self.data_type_combo)
        top_layout.addLayout(data_type_layout)
        
        # Botón para crear la estructura
        create_layout = QVBoxLayout()
        create_layout.addStretch()
        self.create_btn = QPushButton("Crear Estructura")
        create_layout.addWidget(self.create_btn)
        top_layout.addLayout(create_layout)
        
        # Añadir la sección superior al layout principal
        main_layout.addWidget(top_section, 1)
        
        # Sección central: Panel de visualización
        self.structure_panels = QStackedWidget()
        
        # Crear paneles para cada estructura
        self.stack_panel = StackPanel()
        self.queue_panel = QueuePanel()
        self.linked_list_panel = LinkedListPanel()
        self.circular_list_panel = CircularListPanel()
        self.doubly_linked_list_panel = DoublyLinkedListPanel()
        self.binary_tree_panel = BinaryTreePanel()
        self.binary_search_tree_panel = BinarySearchTreePanel()
        
        # Añadir paneles al stacked widget
        self.structure_panels.addWidget(self.stack_panel)
        self.structure_panels.addWidget(self.queue_panel)
        self.structure_panels.addWidget(self.linked_list_panel)
        self.structure_panels.addWidget(self.circular_list_panel)
        self.structure_panels.addWidget(self.doubly_linked_list_panel)
        self.structure_panels.addWidget(self.binary_tree_panel)
        self.structure_panels.addWidget(self.binary_search_tree_panel)
        
        # Panel inicial
        self.structure_panels.setCurrentIndex(0)
        
        # Añadir panel al layout principal
        main_layout.addWidget(self.structure_panels, 4)
        
        # Conectar eventos
        self.structure_combo.currentIndexChanged.connect(self.structure_changed)
        self.create_btn.clicked.connect(self.create_structure)
    
    def structure_changed(self, index):
        """
        Evento al cambiar la estructura de datos seleccionada.
        
        Args:
            index: Índice de la estructura seleccionada
        """
        self.structure_panels.setCurrentIndex(index)
    
    def create_structure(self):
        """
        Crea la estructura de datos seleccionada.
        """
        # Obtener el tipo de dato seleccionado
        data_type_index = self.data_type_combo.currentIndex()
        data_type = [
            DataType.INTEGER,
            DataType.FLOAT,
            DataType.BOOLEAN,
            DataType.STRING,
            DataType.OBJECT
        ][data_type_index]
        
        # Obtener el panel actual
        current_panel = self.structure_panels.currentWidget()
        
        # Crear la estructura
        current_panel.create_structure(data_type) 