from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout, QSpinBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from gui.base_panel import BasePanel
from structures.doubly_linked_list import DoublyLinkedList
from utils.graph_utils import generate_doubly_linked_list_graph

class DoublyLinkedListPanel(BasePanel):
    """
    Panel para visualizar y manipular listas doblemente enlazadas.
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
        
        button_layout = QHBoxLayout()
        self.insert_at_beginning_button = QPushButton("Insertar al Inicio")
        self.insert_at_beginning_button.clicked.connect(self.insert_at_beginning)
        
        self.insert_at_end_button = QPushButton("Insertar al Final")
        self.insert_at_end_button.clicked.connect(self.insert_at_end)
        
        button_layout.addWidget(self.insert_at_beginning_button)
        button_layout.addWidget(self.insert_at_end_button)
        
        # Control de posición
        position_layout = QHBoxLayout()
        position_layout.addWidget(QLabel("Posición:"))
        self.position_spinbox = QSpinBox()
        self.position_spinbox.setMinimum(0)
        self.position_spinbox.setMaximum(9999)
        self.position_spinbox.setValue(0)
        position_layout.addWidget(self.position_spinbox)
        
        self.insert_at_position_button = QPushButton("Insertar en Posición")
        self.insert_at_position_button.clicked.connect(self.insert_at_position)
        
        insert_layout.addLayout(input_layout)
        insert_layout.addLayout(button_layout)
        insert_layout.addLayout(position_layout)
        insert_layout.addWidget(self.insert_at_position_button)
        
        self.operations_layout.addWidget(insert_group)
        
        # Grupo para eliminar
        remove_group = QGroupBox("Eliminar")
        remove_layout = QVBoxLayout(remove_group)
        
        self.remove_from_beginning_button = QPushButton("Eliminar del Inicio")
        self.remove_from_beginning_button.clicked.connect(self.remove_from_beginning)
        
        self.remove_from_end_button = QPushButton("Eliminar del Final")
        self.remove_from_end_button.clicked.connect(self.remove_from_end)
        
        # Control de posición para eliminar
        remove_position_layout = QHBoxLayout()
        remove_position_layout.addWidget(QLabel("Posición:"))
        self.remove_position_spinbox = QSpinBox()
        self.remove_position_spinbox.setMinimum(0)
        self.remove_position_spinbox.setMaximum(9999)
        self.remove_position_spinbox.setValue(0)
        remove_position_layout.addWidget(self.remove_position_spinbox)
        
        self.remove_at_position_button = QPushButton("Eliminar en Posición")
        self.remove_at_position_button.clicked.connect(self.remove_at_position)
        
        remove_layout.addWidget(self.remove_from_beginning_button)
        remove_layout.addWidget(self.remove_from_end_button)
        remove_layout.addLayout(remove_position_layout)
        remove_layout.addWidget(self.remove_at_position_button)
        
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
        
        # Botón para limpiar la lista
        self.clear_button = QPushButton("Limpiar Lista")
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
        self.insert_at_beginning_button.setEnabled(enabled)
        self.insert_at_end_button.setEnabled(enabled)
        self.insert_at_position_button.setEnabled(enabled)
        self.remove_from_beginning_button.setEnabled(enabled)
        self.remove_from_end_button.setEnabled(enabled)
        self.remove_at_position_button.setEnabled(enabled)
        self.search_button.setEnabled(enabled)
        self.clear_button.setEnabled(enabled)
        self.insert_input.setEnabled(enabled)
        self.search_input.setEnabled(enabled)
        self.position_spinbox.setEnabled(enabled)
        self.remove_position_spinbox.setEnabled(enabled)
    
    def create_structure(self, data_type):
        """
        Crea una nueva lista doblemente enlazada con el tipo de dato especificado.
        
        Args:
            data_type: Tipo de datos para la lista
        """
        self.structure = DoublyLinkedList(data_type)
        self._set_controls_enabled(True)
        self.update_info()
        self.update_visualization()
        self.show_message("Estructura Creada", "Se ha creado una nueva lista doblemente enlazada vacía.")
    
    def insert_at_beginning(self):
        """
        Inserta un nuevo elemento al inicio de la lista.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        value = self.insert_input.text().strip()
        if not value:
            self.show_error("Error", "Debe ingresar un valor.")
            return
        
        success = self.structure.insert_at_beginning(value)
        if success:
            self.insert_input.clear()
            self.update_info()
            self.update_visualization()
            self.show_message("Operación Exitosa", f"Se ha insertado el valor {value} al inicio de la lista.")
        else:
            self.show_error("Error", f"No se pudo insertar el valor {value}. Verifique que sea del tipo correcto.")
    
    def insert_at_end(self):
        """
        Inserta un nuevo elemento al final de la lista.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        value = self.insert_input.text().strip()
        if not value:
            self.show_error("Error", "Debe ingresar un valor.")
            return
        
        success = self.structure.insert_at_end(value)
        if success:
            self.insert_input.clear()
            self.update_info()
            self.update_visualization()
            self.show_message("Operación Exitosa", f"Se ha insertado el valor {value} al final de la lista.")
        else:
            self.show_error("Error", f"No se pudo insertar el valor {value}. Verifique que sea del tipo correcto.")
    
    def insert_at_position(self):
        """
        Inserta un nuevo elemento en una posición específica de la lista.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        value = self.insert_input.text().strip()
        if not value:
            self.show_error("Error", "Debe ingresar un valor.")
            return
        
        position = self.position_spinbox.value()
        
        success = self.structure.insert_at_position(value, position)
        if success:
            self.insert_input.clear()
            self.update_info()
            self.update_visualization()
            self.show_message("Operación Exitosa", f"Se ha insertado el valor {value} en la posición {position} de la lista.")
        else:
            self.show_error("Error", f"No se pudo insertar el valor {value} en la posición {position}. Verifique que la posición sea válida y el valor sea del tipo correcto.")
    
    def remove_from_beginning(self):
        """
        Elimina y retorna el primer elemento de la lista.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        if self.structure.is_empty():
            self.show_error("Error", "La lista está vacía.")
            return
        
        value = self.structure.remove_from_beginning()
        self.update_info()
        self.update_visualization()
        self.show_message("Operación Exitosa", f"Se ha eliminado el valor {value} del inicio de la lista.")
    
    def remove_from_end(self):
        """
        Elimina y retorna el último elemento de la lista.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        if self.structure.is_empty():
            self.show_error("Error", "La lista está vacía.")
            return
        
        value = self.structure.remove_from_end()
        self.update_info()
        self.update_visualization()
        self.show_message("Operación Exitosa", f"Se ha eliminado el valor {value} del final de la lista.")
    
    def remove_at_position(self):
        """
        Elimina y retorna el elemento en una posición específica de la lista.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        if self.structure.is_empty():
            self.show_error("Error", "La lista está vacía.")
            return
        
        position = self.remove_position_spinbox.value()
        
        if position >= self.structure.size:
            self.show_error("Error", f"Posición inválida. La lista tiene {self.structure.size} elementos.")
            return
        
        value = self.structure.remove_at_position(position)
        
        if value is not None:
            self.update_info()
            self.update_visualization()
            self.show_message("Operación Exitosa", f"Se ha eliminado el valor {value} de la posición {position} de la lista.")
        else:
            self.show_error("Error", f"No se pudo eliminar el elemento en la posición {position}.")
    
    def search(self):
        """
        Busca un valor en la lista.
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
            self.show_message("Búsqueda", f"El valor {value} se encuentra en la lista.")
        else:
            self.show_message("Búsqueda", f"El valor {value} no se encuentra en la lista.")
        
        self.search_input.clear()
    
    def clear(self):
        """
        Vacía la lista completamente.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        self.structure.clear()
        self.update_info()
        self.update_visualization()
        self.show_message("Operación Exitosa", "Se ha vaciado la lista.")
    
    def update_visualization(self):
        """
        Actualiza la visualización gráfica de la lista.
        """
        if not self.structure:
            return
        
        # Generar imagen de la lista
        image_path = generate_doubly_linked_list_graph(self.structure)
        
        # Mostrar la imagen
        pixmap = QPixmap(image_path)
        self.visualization_widget.setPixmap(pixmap)
        self.visualization_widget.setAlignment(Qt.AlignCenter) 