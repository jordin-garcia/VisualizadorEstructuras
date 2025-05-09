from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from gui.base_panel import BasePanel
from structures.queue import Queue
from utils.graph_utils import generate_queue_graph

class QueuePanel(BasePanel):
    """
    Panel para visualizar y manipular colas (queues).
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
        
        self.enqueue_button = QPushButton("Insertar (Enqueue)")
        self.enqueue_button.clicked.connect(self.enqueue)
        
        insert_layout.addLayout(input_layout)
        insert_layout.addWidget(self.enqueue_button)
        
        self.operations_layout.addWidget(insert_group)
        
        # Grupo para eliminar
        remove_group = QGroupBox("Eliminar")
        remove_layout = QVBoxLayout(remove_group)
        
        self.dequeue_button = QPushButton("Eliminar (Dequeue)")
        self.dequeue_button.clicked.connect(self.dequeue)
        
        remove_layout.addWidget(self.dequeue_button)
        
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
        
        # Botón para limpiar la cola
        self.clear_button = QPushButton("Limpiar Cola")
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
        self.enqueue_button.setEnabled(enabled)
        self.dequeue_button.setEnabled(enabled)
        self.search_button.setEnabled(enabled)
        self.clear_button.setEnabled(enabled)
        self.insert_input.setEnabled(enabled)
        self.search_input.setEnabled(enabled)
    
    def create_structure(self, data_type):
        """
        Crea una nueva cola con el tipo de dato especificado.
        
        Args:
            data_type: Tipo de datos para la cola
        """
        self.structure = Queue(data_type)
        self._set_controls_enabled(True)
        self.update_info()
        self.update_visualization()
        self.show_message("Estructura Creada", "Se ha creado una nueva cola vacía.")
    
    def enqueue(self):
        """
        Inserta un nuevo elemento en la cola.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        value = self.insert_input.text().strip()
        if not value:
            self.show_error("Error", "Debe ingresar un valor.")
            return
        
        success = self.structure.enqueue(value)
        if success:
            self.insert_input.clear()
            self.update_info()
            self.update_visualization()
            self.show_message("Operación Exitosa", f"Se ha insertado el valor {value} en la cola.")
        else:
            self.show_error("Error", f"No se pudo insertar el valor {value}. Verifique que sea del tipo correcto.")
    
    def dequeue(self):
        """
        Elimina y retorna el elemento del frente de la cola.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        if self.structure.is_empty():
            self.show_error("Error", "La cola está vacía.")
            return
        
        value = self.structure.dequeue()
        self.update_info()
        self.update_visualization()
        self.show_message("Operación Exitosa", f"Se ha eliminado el valor {value} de la cola.")
    
    def search(self):
        """
        Busca un valor en la cola.
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
            self.show_message("Búsqueda", f"El valor {value} se encuentra en la cola.")
        else:
            self.show_message("Búsqueda", f"El valor {value} no se encuentra en la cola.")
        
        self.search_input.clear()
    
    def clear(self):
        """
        Vacía la cola completamente.
        """
        if not self.structure:
            self.show_error("Error", "Debe crear la estructura primero.")
            return
        
        self.structure.clear()
        self.update_info()
        self.update_visualization()
        self.show_message("Operación Exitosa", "Se ha vaciado la cola.")
    
    def update_visualization(self):
        """
        Actualiza la visualización gráfica de la cola.
        """
        if not self.structure:
            return
        
        # Generar imagen de la cola
        image_path = generate_queue_graph(self.structure)
        
        # Mostrar la imagen
        pixmap = QPixmap(image_path)
        self.visualization_widget.setPixmap(pixmap)
        self.visualization_widget.setAlignment(Qt.AlignCenter) 