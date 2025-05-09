from structures.linked_list.node import Node
from utils.data_types import DataType, validate_data, convert_data

class LinkedList:
    """
    Implementación de una lista enlazada simple.
    
    Attributes:
        head: Referencia al primer nodo de la lista
        tail: Referencia al último nodo de la lista
        size: Cantidad de elementos en la lista
        data_type: Tipo de datos que almacena la lista
    """
    
    def __init__(self, data_type=DataType.INTEGER):
        """
        Inicializa una lista enlazada vacía.
        
        Args:
            data_type: Tipo de datos que almacenará la lista (por defecto, enteros)
        """
        self.head = None
        self.tail = None
        self.size = 0
        self.data_type = data_type
    
    def insert_at_beginning(self, data):
        """
        Inserta un elemento al inicio de la lista.
        
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
        
        # Si la lista está vacía, el nuevo nodo es tanto la cabeza como la cola
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            # Insertar al inicio
            new_node.next = self.head
            self.head = new_node
        
        # Incrementar el tamaño
        self.size += 1
        
        return True
    
    def insert_at_end(self, data):
        """
        Inserta un elemento al final de la lista.
        
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
        
        # Si la lista está vacía, el nuevo nodo es tanto la cabeza como la cola
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            # Insertar al final
            self.tail.next = new_node
            self.tail = new_node
        
        # Incrementar el tamaño
        self.size += 1
        
        return True
    
    def remove_from_beginning(self):
        """
        Elimina y retorna el primer elemento de la lista.
        
        Returns:
            El dato eliminado o None si la lista está vacía
        """
        if self.is_empty():
            return None
        
        # Guardar el dato a retornar
        data = self.head.data
        
        # Actualizar la cabeza
        self.head = self.head.next
        
        # Si la cabeza es None, la lista quedó vacía
        if self.head is None:
            self.tail = None
        
        # Reducir el tamaño
        self.size -= 1
        
        return data
    
    def remove_from_end(self):
        """
        Elimina y retorna el último elemento de la lista.
        
        Returns:
            El dato eliminado o None si la lista está vacía
        """
        if self.is_empty():
            return None
        
        # Si solo hay un elemento, es lo mismo que remover del inicio
        if self.head == self.tail:
            return self.remove_from_beginning()
        
        # Buscar el penúltimo nodo
        current = self.head
        while current.next != self.tail:
            current = current.next
        
        # Guardar el dato a retornar
        data = self.tail.data
        
        # Actualizar la cola
        self.tail = current
        self.tail.next = None
        
        # Reducir el tamaño
        self.size -= 1
        
        return data
    
    def search(self, data):
        """
        Busca un elemento en la lista.
        
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
        
        # Recorrer la lista
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        
        return False
    
    def is_empty(self):
        """
        Verifica si la lista está vacía.
        
        Returns:
            bool: True si la lista está vacía, False en caso contrario
        """
        return self.head is None
    
    def clear(self):
        """
        Vacía la lista completamente.
        """
        self.head = None
        self.tail = None
        self.size = 0
    
    def get_info(self):
        """
        Retorna información sobre el estado actual de la lista.
        
        Returns:
            dict: Diccionario con información de la lista
        """
        return {
            "tipo": "Lista Enlazada Simple",
            "tamaño": self.size,
            "tipo_dato": self.data_type.value,
            "cabeza": str(self.head.data) if self.head else "Vacía",
            "cola": str(self.tail.data) if self.tail else "Vacía"
        } 