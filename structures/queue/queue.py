from structures.queue.node import Node
from utils.data_types import DataType, validate_data, convert_data

class Queue:
    """
    Implementación de una cola (FIFO - First In First Out).
    
    Attributes:
        front: Referencia al nodo en el frente de la cola
        rear: Referencia al nodo en el final de la cola
        size: Cantidad de elementos en la cola
        data_type: Tipo de datos que almacena la cola
    """
    
    def __init__(self, data_type=DataType.INTEGER):
        """
        Inicializa una cola vacía.
        
        Args:
            data_type: Tipo de datos que almacenará la cola (por defecto, enteros)
        """
        self.front = None
        self.rear = None
        self.size = 0
        self.data_type = data_type
    
    def enqueue(self, data):
        """
        Inserta un elemento al final de la cola.
        
        Args:
            data: Dato a insertar
            
        Returns:
            bool: True si se insertó correctamente, False en caso contrario
        """
        # Validar que el dato sea del tipo correcto
        if not validate_data(data, self.data_type):
            return False
        
        # Convertir al tipo correcto
        data = convert_data(data, self.data_type)
        
        # Crear nuevo nodo
        new_node = Node(data)
        
        # Si la cola está vacía, el nuevo nodo es tanto el frente como el final
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            # Agregar al final de la cola
            self.rear.next = new_node
            self.rear = new_node
        
        # Incrementar el tamaño
        self.size += 1
        
        return True
    
    def dequeue(self):
        """
        Elimina y retorna el elemento del frente de la cola.
        
        Returns:
            El dato eliminado o None si la cola está vacía
        """
        if self.is_empty():
            return None
        
        # Guardar el dato a retornar
        data = self.front.data
        
        # Actualizar el frente
        self.front = self.front.next
        
        # Si el frente es None, la cola quedó vacía
        if self.front is None:
            self.rear = None
        
        # Reducir el tamaño
        self.size -= 1
        
        return data
    
    def peek(self):
        """
        Retorna el elemento del frente de la cola sin eliminarlo.
        
        Returns:
            El dato en el frente o None si la cola está vacía
        """
        return None if self.is_empty() else self.front.data
    
    def search(self, data):
        """
        Busca un elemento en la cola.
        
        Args:
            data: Dato a buscar
            
        Returns:
            True si se encuentra el dato, False en caso contrario
        """
        if self.is_empty():
            return False
        
        # Convertir al tipo correcto para la comparación
        if validate_data(data, self.data_type):
            data = convert_data(data, self.data_type)
        else:
            return False
        
        # Recorrer la cola
        current = self.front
        while current:
            if current.data == data:
                return True
            current = current.next
        
        return False
    
    def is_empty(self):
        """
        Verifica si la cola está vacía.
        
        Returns:
            bool: True si la cola está vacía, False en caso contrario
        """
        return self.front is None
    
    def clear(self):
        """
        Vacía la cola completamente.
        """
        self.front = None
        self.rear = None
        self.size = 0
    
    def get_info(self):
        """
        Retorna información sobre el estado actual de la cola.
        
        Returns:
            dict: Diccionario con información de la cola
        """
        return {
            "tipo": "Cola",
            "tamaño": self.size,
            "tipo_dato": self.data_type.value,
            "frente": str(self.peek()) if not self.is_empty() else "Vacía",
            "final": str(self.rear.data) if self.rear else "Vacía"
        } 