from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from gui.base_panel import BasePanel
from structures.binary_tree import BinaryTree
from structures.binary_tree.node import Node
from utils.graph_utils import generate_binary_tree_graph
from utils.data_types import validate_data, convert_data

class BinaryTreePanel(BasePanel):
    """
    Panel para visualizar y manipular árboles binarios.
    """
    
    def __init__(self):
        super().__init__()
        
        # Agregar controles específicos
        self._setup_controls()
    
    def _setup_controls(self):
        # Grupo para insertar
        insert_group = QGroupBox("Insertar")
        insert_layout = QVBoxLayout(insert_group)
        
        # Valor a insertar
        value_layout = QHBoxLayout()
        self.insert_input = QLineEdit()
        self.insert_input.setPlaceholderText("Valor a insertar")
        value_layout.addWidget(QLabel("Valor:"))
        value_layout.addWidget(self.insert_input)
        
        # Botón para insertar automáticamente por niveles
        self.insert_button = QPushButton("Insertar Nodo")
        self.insert_button.clicked.connect(self.insert)
        
        insert_layout.addLayout(value_layout)
        insert_layout.addWidget(self.insert_button)
        
        self.operations_layout.addWidget(insert_group)
        
        # Grupo para eliminar
        remove_group = QGroupBox("Eliminar")
        remove_layout = QVBoxLayout(remove_group)
        
        remove_input_layout = QHBoxLayout()
        self.remove_input = QLineEdit()
        self.remove_input.setPlaceholderText("Valor del nodo a eliminar")
        remove_input_layout.addWidget(QLabel("Valor:"))
        remove_input_layout.addWidget(self.remove_input)
        
        self.remove_button = QPushButton("Eliminar Nodo")
        self.remove_button.clicked.connect(self.remove)
        
        remove_layout.addLayout(remove_input_layout)
        remove_layout.addWidget(self.remove_button)
        
        self.operations_layout.addWidget(remove_group)
        
        # Grupo para buscar
        search_group = QGroupBox("Buscar")
        search_layout = QVBoxLayout(search_group)
        
        search_input_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Valor a buscar")
        search_input_layout.addWidget(QLabel("Valor:"))
        search_input_layout.addWidget(self.search_input)
        
        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.search)
        
        search_layout.addLayout(search_input_layout)
        search_layout.addWidget(self.search_button)
        
        self.operations_layout.addWidget(search_group)
        
        # Botón para limpiar el árbol
        self.clear_button = QPushButton("Limpiar Árbol")
        self.clear_button.clicked.connect(self.clear)
        
        self.operations_layout.addWidget(self.clear_button)
        self.operations_layout.addStretch()
        
        # Deshabilitar controles hasta que se cree la estructura
        self._set_controls_enabled(False)
    
    def _set_controls_enabled(self, enabled):
        """
        Habilita o deshabilita los controles de operaciones.
        
        Args:
            enabled: True para habilitar, False para deshabilitar
        """
        self.insert_button.setEnabled(enabled)
        self.remove_button.setEnabled(enabled)
        self.search_button.setEnabled(enabled)
        self.clear_button.setEnabled(enabled)
        self.insert_input.setEnabled(enabled)
        self.remove_input.setEnabled(enabled)
        self.search_input.setEnabled(enabled)
    
    def create_structure(self, data_type):
        """
        Crea un nuevo árbol binario con el tipo de dato especificado.
        
        Args:
            data_type: Tipo de datos para el árbol
        """
        self.structure = BinaryTree(data_type)
        self._set_controls_enabled(True)
        self.update_info()
        self.update_visualization()
        self.show_message("Estructura Creada", "Se ha creado un nuevo árbol binario vacío.")
    
    def insert(self):
        """
        Inserta un nuevo elemento en el árbol utilizando el método de inserción por niveles.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        value = self.insert_input.text().strip()
        if not value:
            self.show_error("Error", "Debe ingresar un valor a insertar.")
            return
        
        success = self.structure.insert(value)
        if success:
            self.insert_input.clear()
            self.update_info()
            self.update_visualization()
            self.show_message("Operación Exitosa", f"Se ha insertado el valor {value} en el árbol.")
        else:
            self.show_error("Error", f"No se pudo insertar el valor {value}. Verifique que sea del tipo correcto.")
    
    def remove(self):
        """
        Elimina un nodo con el valor especificado.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        if self.structure.is_empty():
            self.show_error("Error", "El árbol está vacío.")
            return
        
        value = self.remove_input.text().strip()
        if not value:
            self.show_error("Error", "Debe ingresar un valor a eliminar.")
            return
        
        success = self.structure.remove(value)
        if success:
            self.remove_input.clear()
            self.update_info()
            self.update_visualization()
            self.show_message("Operación Exitosa", f"Se ha eliminado el nodo con valor {value}.")
        else:
            self.show_error("Error", f"No se pudo eliminar el nodo con valor {value}. Verifique que exista y no tenga dos hijos.")
    
    def search(self):
        """
        Busca un valor en el árbol.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        value = self.search_input.text().strip()
        if not value:
            self.show_error("Error", "Debe ingresar un valor a buscar.")
            return
        
        found = self.structure.search(value)
        if found:
            self.show_message("Búsqueda", f"El valor {value} se encuentra en el árbol.")
        else:
            self.show_message("Búsqueda", f"El valor {value} no se encuentra en el árbol.")
        
        self.search_input.clear()
    
    def clear(self):
        """
        Vacía el árbol completamente.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        self.structure.clear()
        self.update_info()
        self.update_visualization()
        self.show_message("Operación Exitosa", "Se ha vaciado el árbol.")
    
    def update_visualization(self):
        """
        Actualiza la visualización gráfica del árbol.
        """
        if not self.structure:
            return
        
        # Generar imagen del árbol
        image_path = generate_binary_tree_graph(self.structure)
        
        # Mostrar la imagen
        pixmap = QPixmap(image_path)
        self.visualization_widget.setPixmap(pixmap)
        self.visualization_widget.setAlignment(Qt.AlignCenter) 