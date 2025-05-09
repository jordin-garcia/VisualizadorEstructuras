class Node:
    """
    Clase que representa un nodo en un árbol binario de búsqueda.
    
    Attributes:
        data: El dato almacenado en el nodo
        left: Referencia al hijo izquierdo
        right: Referencia al hijo derecho
        parent: Referencia al nodo padre
    """
    
    def __init__(self, data):
        """
        Inicializa un nuevo nodo con el dato proporcionado.
        
        Args:
            data: El dato a almacenar en el nodo
        """
        self.data = data
        self.left = None
        self.right = None
        self.parent = None 