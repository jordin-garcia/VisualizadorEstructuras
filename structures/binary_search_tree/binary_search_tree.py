from structures.binary_search_tree.node import Node
from utils.data_types import DataType, validate_data, convert_data

class BinarySearchTree:
    """
    Implementación de un árbol binario de búsqueda.
    
    Attributes:
        root: Referencia al nodo raíz del árbol
        size: Cantidad de elementos en el árbol
        data_type: Tipo de datos que almacena el árbol
    """
    
    def __init__(self, data_type=DataType.INTEGER):
        """
        Inicializa un árbol binario de búsqueda vacío.
        
        Args:
            data_type: Tipo de datos que almacenará el árbol (por defecto, enteros)
        """
        self.root = None
        self.size = 0
        self.data_type = data_type
    
    def insert(self, data):
        """
        Inserta un nuevo elemento en el árbol respetando el orden BST.
        
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
        
        # Si el árbol está vacío, el nuevo nodo es la raíz
        if self.root is None:
            self.root = new_node
            self.size += 1
            return True
        
        # Buscar la posición correcta para insertar
        current = self.root
        while True:
            # Si el dato es menor que el dato del nodo actual, ir al subárbol izquierdo
            if data < current.data:
                # Si no tiene hijo izquierdo, insertar aquí
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    break
                # Si tiene hijo izquierdo, seguir buscando
                current = current.left
            # Si el dato es mayor o igual que el dato del nodo actual, ir al subárbol derecho
            else:
                # Si no tiene hijo derecho, insertar aquí
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    break
                # Si tiene hijo derecho, seguir buscando
                current = current.right
        
        # Incrementar el tamaño
        self.size += 1
        
        return True
    
    def remove(self, data):
        """
        Elimina un nodo con el valor especificado.
        
        Args:
            data: Valor del nodo a eliminar
            
        Returns:
            bool: True si se eliminó correctamente, False en caso contrario
        """
        if self.root is None:
            return False
        
        # Convertir al tipo correcto para la comparación
        if validate_data(data, self.data_type):
            data = convert_data(data, self.data_type)
        else:
            return False
        
        # Buscar el nodo a eliminar
        node_to_remove = self._find_node(data)
        if node_to_remove is None:
            return False
        
        # Caso 1: Nodo sin hijos (nodo hoja)
        if node_to_remove.left is None and node_to_remove.right is None:
            self._remove_leaf(node_to_remove)
        
        # Caso 2: Nodo con un solo hijo
        elif node_to_remove.left is None:
            self._remove_with_one_child(node_to_remove, node_to_remove.right)
        elif node_to_remove.right is None:
            self._remove_with_one_child(node_to_remove, node_to_remove.left)
        
        # Caso 3: Nodo con dos hijos
        else:
            # Encontrar el sucesor (el valor más pequeño en el subárbol derecho)
            successor = self._find_min(node_to_remove.right)
            
            # Copiar el dato del sucesor al nodo a eliminar
            node_to_remove.data = successor.data
            
            # Eliminar el sucesor (que tiene a lo sumo un hijo derecho)
            if successor.right is None:
                self._remove_leaf(successor)
            else:
                self._remove_with_one_child(successor, successor.right)
        
        # Decrementar el tamaño
        self.size -= 1
        
        return True
    
    def _remove_leaf(self, node):
        """
        Elimina un nodo hoja (sin hijos).
        
        Args:
            node: Nodo a eliminar
        """
        # Si es la raíz
        if node == self.root:
            self.root = None
            return
        
        # Determinar si es hijo izquierdo o derecho
        if node.parent.left == node:
            node.parent.left = None
        else:
            node.parent.right = None
    
    def _remove_with_one_child(self, node, child):
        """
        Elimina un nodo con un solo hijo.
        
        Args:
            node: Nodo a eliminar
            child: Hijo del nodo a eliminar
        """
        # Si es la raíz
        if node == self.root:
            self.root = child
            child.parent = None
            return
        
        # Determinar si es hijo izquierdo o derecho
        if node.parent.left == node:
            node.parent.left = child
        else:
            node.parent.right = child
        
        # Actualizar la referencia del padre del hijo
        child.parent = node.parent
    
    def _find_min(self, node):
        """
        Encuentra el nodo con el valor mínimo en el subárbol.
        
        Args:
            node: Raíz del subárbol
            
        Returns:
            Node: Nodo con el valor mínimo
        """
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def search(self, data):
        """
        Busca un nodo con el valor especificado.
        
        Args:
            data: Valor a buscar
            
        Returns:
            bool: True si se encuentra el valor, False en caso contrario
        """
        return self._find_node(data) is not None
    
    def _find_node(self, value):
        """
        Busca un nodo con el valor especificado.
        
        Args:
            value: Valor a buscar
            
        Returns:
            Node: El nodo encontrado o None si no existe
        """
        # Convertir al tipo correcto para la comparación si es necesario
        if validate_data(value, self.data_type):
            value = convert_data(value, self.data_type)
        else:
            return None
        
        current = self.root
        while current is not None:
            if current.data == value:
                return current
            elif value < current.data:
                current = current.left
            else:
                current = current.right
        
        return None
    
    def height(self, node=None):
        """
        Calcula la altura del árbol o de un nodo específico.
        
        Args:
            node: Nodo desde el cual calcular la altura (por defecto, la raíz)
            
        Returns:
            int: Altura del árbol o nada si está vacío
        """
        if node is None:
            node = self.root
        
        if node is None:
            return ""
        
        # Función recursiva auxiliar para calcular la altura
        def calculate_height(current_node):
            if current_node is None:
                return -1
            
            left_height = calculate_height(current_node.left)
            right_height = calculate_height(current_node.right)
            
            return max(left_height, right_height) + 1
        
        # Calcular altura usando la función auxiliar
        return calculate_height(node)
    
    def is_empty(self):
        """
        Verifica si el árbol está vacío.
        
        Returns:
            bool: True si el árbol está vacío, False en caso contrario
        """
        return self.root is None
    
    def clear(self):
        """
        Vacía el árbol completamente.
        """
        self.root = None
        self.size = 0
    
    def get_info(self):
        """
        Retorna información sobre el estado actual del árbol.
        
        Returns:
            dict: Diccionario con información del árbol
        """
        return {
            "tipo": "Árbol Binario de Búsqueda",
            "tamaño": self.size,
            "tipo_dato": self.data_type.value,
            "raíz": str(self.root.data) if self.root else "Vacío",
            "altura": self.height()
        } 