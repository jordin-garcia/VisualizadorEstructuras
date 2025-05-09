from structures.doubly_linked_list.node import Node
from utils.data_types import DataType, validate_data, convert_data

class DoublyLinkedList:
    """
    Implementación de una lista doblemente enlazada.
    
    Attributes:
        head: Referencia al primer nodo de la lista
        tail: Referencia al último nodo de la lista
        size: Cantidad de elementos en la lista
        data_type: Tipo de datos que almacena la lista
    """
    
    def __init__(self, data_type=DataType.INTEGER):
        """
        Inicializa una lista doblemente enlazada vacía.
        
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
            self.head.prev = new_node
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
            new_node.prev = self.tail
            self.tail = new_node
        
        # Incrementar el tamaño
        self.size += 1
        
        return True
    
    def insert_at_position(self, data, position):
        """
        Inserta un elemento en una posición específica de la lista.
        
        Args:
            data: Dato a insertar
            position: Posición donde insertar (0-indexed)
            
        Returns:
            bool: True si se insertó correctamente, False en caso contrario
        """
        # Validar posición
        if position < 0 or position > self.size:
            return False
        
        # Insertar al inicio
        if position == 0:
            return self.insert_at_beginning(data)
        
        # Insertar al final
        if position == self.size:
            return self.insert_at_end(data)
        
        # Validar que el dato sea del tipo correcto
        if not validate_data(data, self.data_type):
            return False
        
        # Convertir al tipo correcto
        data = convert_data(data, self.data_type)
        
        # Crear nuevo nodo
        new_node = Node(data)
        
        # Encontrar el nodo en la posición deseada
        current = self.head
        for _ in range(position):
            current = current.next
        
        # Insertar antes del nodo encontrado
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        
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
        
        # Si solo hay un elemento
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # Eliminar del inicio
            self.head = self.head.next
            self.head.prev = None
        
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
        
        # Si solo hay un elemento
        if self.head == self.tail:
            return self.remove_from_beginning()
        
        # Guardar el dato a retornar
        data = self.tail.data
        
        # Eliminar del final
        self.tail = self.tail.prev
        self.tail.next = None
        
        # Reducir el tamaño
        self.size -= 1
        
        return data
    
    def remove_at_position(self, position):
        """
        Elimina y retorna el elemento en una posición específica de la lista.
        
        Args:
            position: Posición del elemento a eliminar (0-indexed)
            
        Returns:
            El dato eliminado o None si la posición es inválida o la lista está vacía
        """
        # Validar posición
        if position < 0 or position >= self.size or self.is_empty():
            return None
        
        # Eliminar del inicio
        if position == 0:
            return self.remove_from_beginning()
        
        # Eliminar del final
        if position == self.size - 1:
            return self.remove_from_end()
        
        # Encontrar el nodo en la posición deseada
        current = self.head
        for _ in range(position):
            current = current.next
        
        # Guardar el dato a retornar
        data = current.data
        
        # Eliminar el nodo
        current.prev.next = current.next
        current.next.prev = current.prev
        
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
            "tipo": "Lista Doblemente Enlazada",
            "tamaño": self.size,
            "tipo_dato": self.data_type.value,
            "cabeza": str(self.head.data) if self.head else "Vacía",
            "cola": str(self.tail.data) if self.tail else "Vacía"
        } 