from structures.stack.node import Node
from utils.data_types import DataType, validate_data, convert_data

class Stack:
    """
    Implementación de una pila (LIFO - Last In First Out).
    
    Attributes:
        top: Referencia al nodo en el tope de la pila
        size: Cantidad de elementos en la pila
        data_type: Tipo de datos que almacena la pila
    """
    
    def __init__(self, data_type=DataType.INTEGER):
        """
        Inicializa una pila vacía.
        
        Args:
            data_type: Tipo de datos que almacenará la pila (por defecto, enteros)
        """
        self.top = None
        self.size = 0
        self.data_type = data_type
    
    def push(self, data):
        """
        Inserta un elemento en el tope de la pila.
        
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
        
        # Conectar el nuevo nodo a la pila
        new_node.next = self.top
        
        # Actualizar el tope de la pila
        self.top = new_node
        
        # Incrementar el tamaño
        self.size += 1
        
        return True
    
    def pop(self):
        """
        Elimina y retorna el elemento en el tope de la pila.
        
        Returns:
            El dato eliminado o None si la pila está vacía
        """
        if self.is_empty():
            return None
        
        # Guardar el dato a retornar
        data = self.top.data
        
        # Actualizar el tope
        self.top = self.top.next
        
        # Reducir el tamaño
        self.size -= 1
        
        return data
    
    def peek(self):
        """
        Retorna el elemento en el tope de la pila sin eliminarlo.
        
        Returns:
            El dato en el tope o None si la pila está vacía
        """
        return None if self.is_empty() else self.top.data
    
    def search(self, data):
        """
        Busca un elemento en la pila.
        
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
        
        # Recorrer la pila
        current = self.top
        while current:
            if current.data == data:
                return True
            current = current.next
        
        return False
    
    def is_empty(self):
        """
        Verifica si la pila está vacía.
        
        Returns:
            bool: True si la pila está vacía, False en caso contrario
        """
        return self.top is None
    
    def clear(self):
        """
        Vacía la pila completamente.
        """
        self.top = None
        self.size = 0
    
    def get_info(self):
        """
        Retorna información sobre el estado actual de la pila.
        
        Returns:
            dict: Diccionario con información de la pila
        """
        return {
            "tipo": "Pila",
            "tamaño": self.size,
            "tipo_dato": self.data_type.value,
            "tope": str(self.peek()) if not self.is_empty() else "Vacía"
        } 