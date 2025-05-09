class Node:
    """
    Clase que representa un nodo en una pila.
    
    Attributes:
        data: El dato almacenado en el nodo
        next: Referencia al siguiente nodo en la pila
    """
    
    def __init__(self, data):
        """
        Inicializa un nuevo nodo con el dato proporcionado.
        
        Args:
            data: El dato a almacenar en el nodo
        """
        self.data = data
        self.next = None 