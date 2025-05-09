from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from gui.base_panel import BasePanel
from structures.stack import Stack
from utils.graph_utils import generate_stack_graph

class StackPanel(BasePanel):
    """
    Panel para visualizar y manipular pilas (stacks).
    """
    
    def __init__(self):
        super().__init__()
        
        # Agregar controles específicos
        self._setup_controls()
    
    def _setup_controls(self):
        # Grupo para insertar
        insert_group = QGroupBox("Insertar")
        insert_layout = QVBoxLayout(insert_group)
        
        input_layout = QHBoxLayout()
        self.insert_input = QLineEdit()
        self.insert_input.setPlaceholderText("Valor a insertar")
        input_layout.addWidget(QLabel("Valor:"))
        input_layout.addWidget(self.insert_input)
        
        self.push_button = QPushButton("Insertar (Push)")
        self.push_button.clicked.connect(self.push)
        
        insert_layout.addLayout(input_layout)
        insert_layout.addWidget(self.push_button)
        
        self.operations_layout.addWidget(insert_group)
        
        # Grupo para eliminar
        remove_group = QGroupBox("Eliminar")
        remove_layout = QVBoxLayout(remove_group)
        
        self.pop_button = QPushButton("Eliminar (Pop)")
        self.pop_button.clicked.connect(self.pop)
        
        remove_layout.addWidget(self.pop_button)
        
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
        
        # Botón para limpiar la pila
        self.clear_button = QPushButton("Limpiar Pila")
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
        self.push_button.setEnabled(enabled)
        self.pop_button.setEnabled(enabled)
        self.search_button.setEnabled(enabled)
        self.clear_button.setEnabled(enabled)
        self.insert_input.setEnabled(enabled)
        self.search_input.setEnabled(enabled)
    
    def create_structure(self, data_type):
        """
        Crea una nueva pila con el tipo de dato especificado.
        
        Args:
            data_type: Tipo de datos para la pila
        """
        self.structure = Stack(data_type)
        self._set_controls_enabled(True)
        self.update_info()
        self.update_visualization()
        self.show_message("Estructura Creada", "Se ha creado una nueva pila vacía.")
    
    def push(self):
        """
        Inserta un nuevo elemento en la pila.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        value = self.insert_input.text().strip()
        if not value:
            self.show_error("Error", "Debe ingresar un valor.")
            return
        
        success = self.structure.push(value)
        if success:
            self.insert_input.clear()
            self.update_info()
            self.update_visualization()
            self.show_message("Operación Exitosa", f"Se ha insertado el valor {value} en la pila.")
        else:
            self.show_error("Error", f"No se pudo insertar el valor {value}. Verifique que sea del tipo correcto.")
    
    def pop(self):
        """
        Elimina y retorna el elemento superior de la pila.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        if self.structure.is_empty():
            self.show_error("Error", "La pila está vacía.")
            return
        
        value = self.structure.pop()
        self.update_info()
        self.update_visualization()
        self.show_message("Operación Exitosa", f"Se ha eliminado el valor {value} de la pila.")
    
    def search(self):
        """
        Busca un valor en la pila.
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
            self.show_message("Búsqueda", f"El valor {value} se encuentra en la pila.")
        else:
            self.show_message("Búsqueda", f"El valor {value} no se encuentra en la pila.")
        
        self.search_input.clear()
    
    def clear(self):
        """
        Vacía la pila completamente.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        self.structure.clear()
        self.update_info()
        self.update_visualization()
        self.show_message("Operación Exitosa", "Se ha vaciado la pila.")
    
    def update_visualization(self):
        """
        Actualiza la visualización gráfica de la pila.
        """
        if not self.structure:
            return
        
        # Generar imagen de la pila
        image_path = generate_stack_graph(self.structure)
        
        # Mostrar la imagen
        pixmap = QPixmap(image_path)
        self.visualization_widget.setPixmap(pixmap)
        self.visualization_widget.setAlignment(Qt.AlignCenter) 