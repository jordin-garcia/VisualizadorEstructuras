from structures.circular_list.node import Node
from utils.data_types import DataType, validate_data, convert_data

class CircularList:
    """
    Implementación de una lista circular.
    
    Attributes:
        head: Referencia al primer nodo de la lista (que también es la referencia al último nodo)
        size: Cantidad de elementos en la lista
        data_type: Tipo de datos que almacena la lista
    """
    
    def __init__(self, data_type=DataType.INTEGER):
        """
        Inicializa una lista circular vacía.
        
        Args:
            data_type: Tipo de datos que almacenará la lista (por defecto, enteros)
        """
        self.head = None
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
        
        # Si la lista está vacía, el nuevo nodo apunta a sí mismo
        if self.is_empty():
            new_node.next = new_node
            self.head = new_node
        else:
            # Buscar el último nodo
            last = self.head
            while last.next != self.head:
                last = last.next
            
            # Insertar al inicio
            new_node.next = self.head
            self.head = new_node
            
            # El último nodo ahora apunta al nuevo nodo inicial
            last.next = self.head
        
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
        
        # Si la lista está vacía, el nuevo nodo apunta a sí mismo
        if self.is_empty():
            new_node.next = new_node
            self.head = new_node
        else:
            # Buscar el último nodo
            last = self.head
            while last.next != self.head:
                last = last.next
            
            # Insertar al final
            last.next = new_node
            new_node.next = self.head
        
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
        if self.head.next == self.head:
            self.head = None
        else:
            # Buscar el último nodo
            last = self.head
            while last.next != self.head:
                last = last.next
            
            # Actualizar la referencia circular
            self.head = self.head.next
            last.next = self.head
        
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
        if self.head.next == self.head:
            return self.remove_from_beginning()
        
        # Buscar el penúltimo nodo
        current = self.head
        while current.next.next != self.head:
            current = current.next
        
        # Guardar el dato a retornar
        data = current.next.data
        
        # Actualizar la referencia circular
        current.next = self.head
        
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
        while True:
            if current.data == data:
                return True
            current = current.next
            # Verificar si hemos vuelto al principio
            if current == self.head:
                break
        
        return False
    
    def rotate_left(self, positions=1):
        """
        Rota la lista hacia la izquierda (el segundo elemento se convierte en el primero).
        
        Args:
            positions: Número de posiciones a rotar
            
        Returns:
            bool: True si se rotó correctamente, False si la lista está vacía o tiene un solo elemento
        """
        if self.is_empty() or self.size == 1:
            return False
        
        # Normalizar posiciones
        positions = positions % self.size
        if positions == 0:
            return True
        
        # Realizar la rotación
        for _ in range(positions):
            self.head = self.head.next
        
        return True
    
    def rotate_right(self, positions=1):
        """
        Rota la lista hacia la derecha (el último elemento se convierte en el primero).
        
        Args:
            positions: Número de posiciones a rotar
            
        Returns:
            bool: True si se rotó correctamente, False si la lista está vacía o tiene un solo elemento
        """
        if self.is_empty() or self.size == 1:
            return False
        
        # Normalizar posiciones
        positions = positions % self.size
        if positions == 0:
            return True
        
        # Rotar a la derecha es equivalente a rotar a la izquierda (size - positions) veces
        return self.rotate_left(self.size - positions)
    
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
        self.size = 0
    
    def get_info(self):
        """
        Retorna información sobre el estado actual de la lista.
        
        Returns:
            dict: Diccionario con información de la lista
        """
        return {
            "tipo": "Lista Circular",
            "tamaño": self.size,
            "tipo_dato": self.data_type.value,
            "cabeza": str(self.head.data) if self.head else "Vacía"
        } 