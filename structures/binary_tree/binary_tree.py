from structures.binary_tree.node import Node
from utils.data_types import DataType, validate_data, convert_data
from collections import deque

class BinaryTree:
    """
    Implementación de un árbol binario.
    
    Attributes:
        root: Referencia al nodo raíz del árbol
        size: Cantidad de elementos en el árbol
        data_type: Tipo de datos que almacena el árbol
    """
    
    def __init__(self, data_type=DataType.INTEGER):
        """
        Inicializa un árbol binario vacío.
        
        Args:
            data_type: Tipo de datos que almacenará el árbol (por defecto, enteros)
        """
        self.root = None
        self.size = 0
        self.data_type = data_type
    
    def insert(self, data):
        """
        Inserta un nuevo elemento en el primer espacio disponible del árbol, 
        siguiendo un orden por niveles.
        
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
        
        # Usamos BFS para encontrar el primer nodo que no tenga ambos hijos
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            
            # Si no tiene hijo izquierdo, insertamos aquí
            if current.left is None:
                current.left = new_node
                new_node.parent = current
                self.size += 1
                return True
            
            # Si no tiene hijo derecho, insertamos aquí
            if current.right is None:
                current.right = new_node
                new_node.parent = current
                self.size += 1
                return True
            
            # Añadir los hijos a la cola para seguir buscando
            queue.append(current.left)
            queue.append(current.right)
        
        # No debería llegar aquí en un árbol binario válido
        return False
    
    def insert_left(self, parent_value, data):
        """
        Inserta un nodo como hijo izquierdo del nodo con el valor especificado.
        Esta función se mantiene por compatibilidad, pero para inserción automática por niveles
        se recomienda usar insert().
        
        Args:
            parent_value: Valor del nodo padre donde se insertará
            data: Dato a insertar
            
        Returns:
            bool: True si se insertó correctamente, False en caso contrario
        """
        # Validar que el dato sea del tipo correcto
        if not validate_data(data, self.data_type):
            return False
        
        # Convertir al tipo correcto
        data = convert_data(data, self.data_type)
        
        # Si el árbol está vacío, insertar como raíz
        if self.root is None:
            self.root = Node(data)
            self.size += 1
            return True
        
        # Buscar el nodo padre
        parent_node = self._find_node(self.root, parent_value)
        if parent_node is None:
            return False
        
        # Si ya tiene hijo izquierdo, no se puede insertar
        if parent_node.left is not None:
            return False
        
        # Crear e insertar nuevo nodo
        new_node = Node(data)
        parent_node.left = new_node
        new_node.parent = parent_node
        
        # Incrementar el tamaño
        self.size += 1
        
        return True
    
    def insert_right(self, parent_value, data):
        """
        Inserta un nodo como hijo derecho del nodo con el valor especificado.
        Esta función se mantiene por compatibilidad, pero para inserción automática por niveles
        se recomienda usar insert().
        
        Args:
            parent_value: Valor del nodo padre donde se insertará
            data: Dato a insertar
            
        Returns:
            bool: True si se insertó correctamente, False en caso contrario
        """
        # Validar que el dato sea del tipo correcto
        if not validate_data(data, self.data_type):
            return False
        
        # Convertir al tipo correcto
        data = convert_data(data, self.data_type)
        
        # Si el árbol está vacío, insertar como raíz
        if self.root is None:
            self.root = Node(data)
            self.size += 1
            return True
        
        # Buscar el nodo padre
        parent_node = self._find_node(self.root, parent_value)
        if parent_node is None:
            return False
        
        # Si ya tiene hijo derecho, no se puede insertar
        if parent_node.right is not None:
            return False
        
        # Crear e insertar nuevo nodo
        new_node = Node(data)
        parent_node.right = new_node
        new_node.parent = parent_node
        
        # Incrementar el tamaño
        self.size += 1
        
        return True
    
    def remove(self, data):
        """
        Elimina un nodo con el valor especificado.
        Al eliminar un nodo, todos los nodos que vienen después (en orden de niveles)
        se recorren una posición hacia atrás para mantener la estructura compacta.
        
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
        
        # Obtener todos los nodos en orden por niveles
        nodes = self._get_nodes_level_order()
        
        # Buscar el índice del nodo a eliminar
        node_to_remove_index = -1
        for i, node in enumerate(nodes):
            if node.data == data:
                node_to_remove_index = i
                break
        
        # Si no se encontró el nodo, retornar falso
        if node_to_remove_index == -1:
            return False
        
        # Si es el último nodo, simplemente elimínalo
        if node_to_remove_index == len(nodes) - 1:
            parent = nodes[node_to_remove_index].parent
            if parent is None:  # Es la raíz y el único nodo
                self.root = None
            else:
                if parent.left == nodes[node_to_remove_index]:
                    parent.left = None
                else:
                    parent.right = None
            
            self.size -= 1
            return True
            
        # Mover todos los nodos subsiguientes una posición hacia atrás
        for i in range(node_to_remove_index, len(nodes) - 1):
            nodes[i].data = nodes[i + 1].data
        
        # Eliminar el último nodo
        last_node = nodes[-1]
        parent = last_node.parent
        if parent.left == last_node:
            parent.left = None
        else:
            parent.right = None
        
        # Decrementar el tamaño
        self.size -= 1
        
        return True
    
    def _get_nodes_level_order(self):
        """
        Obtiene todos los nodos del árbol en orden por niveles (de izquierda a derecha).
        
        Returns:
            list: Lista de nodos en orden por niveles
        """
        if self.root is None:
            return []
        
        nodes = []
        queue = deque([self.root])
        
        while queue:
            current = queue.popleft()
            nodes.append(current)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return nodes
    
    def search(self, data):
        """
        Busca un nodo con el valor especificado.
        
        Args:
            data: Valor a buscar
            
        Returns:
            bool: True si se encuentra el valor, False en caso contrario
        """
        if self.root is None:
            return False
        
        # Convertir al tipo correcto para la comparación
        if validate_data(data, self.data_type):
            data = convert_data(data, self.data_type)
        else:
            return False
        
        return self._find_node(self.root, data) is not None
    
    def _find_node(self, node, value):
        """
        Busca recursivamente un nodo con el valor especificado.
        
        Args:
            node: Nodo actual a examinar
            value: Valor a buscar
            
        Returns:
            Node: El nodo encontrado o None si no existe
        """
        if node is None:
            return None
        
        # Realizar la comparación adecuada según el tipo de dato
        try:
            node_value = convert_data(node.data, self.data_type)
            search_value = convert_data(value, self.data_type)
            
            if node_value == search_value:
                return node
        except:
            # Si hay error en la conversión, hacer la comparación directa
            if node.data == value:
                return node
        
        # Buscar en el subárbol izquierdo
        left_result = self._find_node(node.left, value)
        if left_result is not None:
            return left_result
        
        # Buscar en el subárbol derecho
        return self._find_node(node.right, value)
    
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
            "tipo": "Árbol Binario",
            "tamaño": self.size,
            "tipo_dato": self.data_type.value,
            "raíz": str(self.root.data) if self.root else "Vacío",
            "altura": self.height()
        } 