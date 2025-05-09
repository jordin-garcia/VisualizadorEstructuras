class Node:
    """
    Clase que representa un nodo en una lista enlazada simple.
    
    Attributes:
        data: El dato almacenado en el nodo
        next: Referencia al siguiente nodo en la lista
    """
    
    def __init__(self, data):
        """
        Inicializa un nuevo nodo con el dato proporcionado.
        
        Args:
            data: El dato a almacenar en el nodo
        """
        self.data = data
        self.next = None 