class Node:
    """
    Clase que representa un nodo en una cola.
    
    Attributes:
        data: El dato almacenado en el nodo
        next: Referencia al siguiente nodo en la cola
    """
    
    def __init__(self, data):
        """
        Inicializa un nuevo nodo con el dato proporcionado.
        
        Args:
            data: El dato a almacenar en el nodo
        """
        self.data = data
        self.next = None 