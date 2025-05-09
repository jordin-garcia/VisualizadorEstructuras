import os
import tempfile
from graphviz import Digraph

def generate_dot_graph(structure_name, nodes, edges, node_attributes=None, graph_attributes=None):
    """
    Genera un gráfico DOT para visualizar la estructura de datos.
    
    Args:
        structure_name: Nombre de la estructura
        nodes: Lista de nodos a mostrar, cada nodo debe ser un diccionario {'id': id, 'label': label}
        edges: Lista de conexiones entre nodos, cada conexión debe ser un diccionario {'from': id_origen, 'to': id_destino, 'label': etiqueta}
        node_attributes: Atributos adicionales para los nodos
        graph_attributes: Atributos adicionales para el gráfico
    
    Returns:
        Objeto Digraph de Graphviz
    """
    # Configuración del gráfico
    dot = Digraph(structure_name, comment=f'Visualización de {structure_name}')
    dot.attr('graph', rankdir='LR')  # Orientación de izquierda a derecha
    
    # Aplicar atributos adicionales al gráfico
    if graph_attributes:
        for key, value in graph_attributes.items():
            dot.attr('graph', **{key: value})
    
    # Agregar nodos
    for node in nodes:
        attrs = {'label': node['label'], 'shape': 'box', 'style': 'filled', 'fillcolor': 'lightblue'}
        
        # Combinar con atributos adicionales si existen
        if node_attributes and node['id'] in node_attributes:
            attrs.update(node_attributes[node['id']])
        
        dot.node(str(node['id']), **attrs)
    
    # Agregar conexiones
    for edge in edges:
        dot.edge(str(edge['from']), str(edge['to']), label=edge.get('label', ''))
    
    return dot

def save_graph_image(dot, filename='structure_graph'):
    """
    Guarda el gráfico como imagen y retorna la ruta del archivo.
    
    Args:
        dot: Objeto Digraph de Graphviz
        filename: Nombre del archivo sin extensión
    
    Returns:
        Ruta al archivo de imagen generado
    """
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, filename)
    
    # Renderizar imagen
    dot.render(filename=file_path, format='png', cleanup=True)
    
    return f"{file_path}.png"

# Funciones específicas para cada tipo de estructura

def generate_stack_graph(stack):
    """
    Genera un gráfico para una pila (Stack).
    
    Args:
        stack: Objeto Stack
        
    Returns:
        Ruta a la imagen generada
    """
    nodes = []
    edges = []
    
    current = stack.top
    prev_id = None
    
    while current:
        node_id = id(current)
        nodes.append({
            'id': node_id,
            'label': f"Valor: {current.data}"
        })
        
        if prev_id:
            edges.append({
                'from': prev_id,
                'to': node_id,
                'label': ""
            })
        
        prev_id = node_id
        current = current.next
    
    # Si la pila está vacía, mostrar un nodo vacío
    if not nodes:
        nodes.append({
            'id': 0,
            'label': "Pila vacía"
        })
    
    # Agregar etiquetas para indicar el tope de la pila
    graph_attrs = {}
    node_attrs = {}
    
    if nodes:
        node_attrs[nodes[0]['id']] = {'fillcolor': 'lightgreen', 'label': f"{nodes[0]['label']}\n(Tope)"}
    
    dot = generate_dot_graph("Pila", nodes, edges, node_attrs, graph_attrs)
    return save_graph_image(dot, "stack_graph")

def generate_queue_graph(queue):
    """
    Genera un gráfico para una cola (Queue).
    
    Args:
        queue: Objeto Queue
        
    Returns:
        Ruta a la imagen generada
    """
    nodes = []
    edges = []
    
    current = queue.front
    prev_id = None
    
    while current:
        node_id = id(current)
        nodes.append({
            'id': node_id,
            'label': f"Valor: {current.data}"
        })
        
        if prev_id:
            edges.append({
                'from': prev_id,
                'to': node_id,
                'label': ""
            })
        
        prev_id = node_id
        current = current.next
    
    # Si la cola está vacía, mostrar un nodo vacío
    if not nodes:
        nodes.append({
            'id': 0,
            'label': "Cola vacía"
        })
    
    # Agregar etiquetas para indicar el frente y el final de la cola
    graph_attrs = {}
    node_attrs = {}
    
    if nodes:
        node_attrs[nodes[0]['id']] = {'fillcolor': 'lightgreen', 'label': f"{nodes[0]['label']}\n(Frente)"}
        if len(nodes) > 1:
            node_attrs[nodes[-1]['id']] = {'fillcolor': 'lightyellow', 'label': f"{nodes[-1]['label']}\n(Final)"}
    
    dot = generate_dot_graph("Cola", nodes, edges, node_attrs, graph_attrs)
    return save_graph_image(dot, "queue_graph")

def generate_linked_list_graph(linked_list):
    """
    Genera un gráfico para una lista enlazada simple.
    
    Args:
        linked_list: Objeto LinkedList
        
    Returns:
        Ruta a la imagen generada
    """
    nodes = []
    edges = []
    
    current = linked_list.head
    prev_id = None
    
    while current:
        node_id = id(current)
        nodes.append({
            'id': node_id,
            'label': f"Valor: {current.data}"
        })
        
        if prev_id:
            edges.append({
                'from': prev_id,
                'to': node_id,
                'label': ""
            })
        
        prev_id = node_id
        current = current.next
    
    # Si la lista está vacía, mostrar un nodo vacío
    if not nodes:
        nodes.append({
            'id': 0,
            'label': "Lista vacía"
        })
    
    # Agregar etiquetas para cabeza y cola
    graph_attrs = {}
    node_attrs = {}
    
    if nodes and len(nodes) > 0:
        node_attrs[nodes[0]['id']] = {'fillcolor': 'lightgreen', 'label': f"{nodes[0]['label']}\n(Cabeza)"}
        if len(nodes) > 1:
            node_attrs[nodes[-1]['id']] = {'fillcolor': 'lightyellow', 'label': f"{nodes[-1]['label']}\n(Cola)"}
    
    dot = generate_dot_graph("Lista Enlazada", nodes, edges, node_attrs, graph_attrs)
    return save_graph_image(dot, "linked_list_graph")

def generate_circular_list_graph(circular_list):
    """
    Genera un gráfico para una lista circular.
    
    Args:
        circular_list: Objeto CircularList
        
    Returns:
        Ruta a la imagen generada
    """
    nodes = []
    edges = []
    
    if not circular_list.head:
        nodes.append({
            'id': 0,
            'label': "Lista vacía"
        })
    else:
        current = circular_list.head
        first_id = id(current)
        prev_id = None
        
        # Recorrer la lista hasta volver a la cabeza
        while True:
            node_id = id(current)
            nodes.append({
                'id': node_id,
                'label': f"Valor: {current.data}"
            })
            
            if prev_id:
                edges.append({
                    'from': prev_id,
                    'to': node_id,
                    'label': ""
                })
            
            prev_id = node_id
            current = current.next
            
            # Si volvimos a la cabeza, cerrar el círculo y terminar
            if current == circular_list.head:
                edges.append({
                    'from': prev_id,
                    'to': first_id,
                    'label': ""
                })
                break
    
    # Marcar la cabeza de la lista
    graph_attrs = {'rankdir': 'TB'}  # Orientación de arriba a abajo para mejor visualización circular
    node_attrs = {}
    
    if nodes and len(nodes) > 0 and circular_list.head:
        node_attrs[nodes[0]['id']] = {'fillcolor': 'lightgreen', 'label': f"{nodes[0]['label']}\n(Cabeza)"}
    
    dot = generate_dot_graph("Lista Circular", nodes, edges, node_attrs, graph_attrs)
    return save_graph_image(dot, "circular_list_graph")

def generate_doubly_linked_list_graph(doubly_list):
    """
    Genera un gráfico para una lista doblemente enlazada.
    
    Args:
        doubly_list: Objeto DoublyLinkedList
        
    Returns:
        Ruta a la imagen generada
    """
    nodes = []
    edges = []
    
    current = doubly_list.head
    prev_id = None
    
    while current:
        node_id = id(current)
        nodes.append({
            'id': node_id,
            'label': f"Valor: {current.data}"
        })
        
        if prev_id:
            # Enlace hacia adelante
            edges.append({
                'from': prev_id,
                'to': node_id,
                'label': "next"
            })
            # Enlace hacia atrás
            edges.append({
                'from': node_id,
                'to': prev_id,
                'label': "prev"
            })
        
        prev_id = node_id
        current = current.next
    
    # Si la lista está vacía, mostrar un nodo vacío
    if not nodes:
        nodes.append({
            'id': 0,
            'label': "Lista vacía"
        })
    
    # Etiquetar cabeza y cola
    graph_attrs = {}
    node_attrs = {}
    
    if nodes and len(nodes) > 0:
        node_attrs[nodes[0]['id']] = {'fillcolor': 'lightgreen', 'label': f"{nodes[0]['label']}\n(Cabeza)"}
        if len(nodes) > 1:
            node_attrs[nodes[-1]['id']] = {'fillcolor': 'lightyellow', 'label': f"{nodes[-1]['label']}\n(Cola)"}
    
    dot = generate_dot_graph("Lista Doblemente Enlazada", nodes, edges, node_attrs, graph_attrs)
    return save_graph_image(dot, "doubly_linked_list_graph")

def generate_binary_tree_graph(binary_tree):
    """
    Genera un gráfico para un árbol binario.
    
    Args:
        binary_tree: Objeto BinaryTree
        
    Returns:
        Ruta a la imagen generada
    """
    nodes = []
    edges = []
    
    # Función recursiva para recorrer el árbol
    def traverse(node, node_id=None, is_left=None):
        if node is None:
            return
        
        current_id = id(node)
        nodes.append({
            'id': current_id,
            'label': f"Valor: {node.data}"
        })
        
        # Si es llamada desde un nodo padre, agregar la conexión
        if node_id is not None:
            edge_label = "izq" if is_left else "der"
            edges.append({
                'from': node_id,
                'to': current_id,
                'label': edge_label
            })
        
        # Recorrer hijos
        if node.left:
            traverse(node.left, current_id, True)
        
        if node.right:
            traverse(node.right, current_id, False)
    
    # Iniciar recorrido desde la raíz
    if binary_tree.root:
        traverse(binary_tree.root)
    
    # Si el árbol está vacío, mostrar un nodo vacío
    if not nodes:
        nodes.append({
            'id': 0,
            'label': "Árbol vacío"
        })
    
    # Marcar la raíz
    graph_attrs = {'rankdir': 'TB'}  # Orientación de arriba a abajo
    node_attrs = {}
    
    if binary_tree.root and nodes:
        root_id = id(binary_tree.root)
        node_attrs[root_id] = {'fillcolor': 'lightgreen', 'label': f"{nodes[0]['label']}\n(Raíz)"}
    
    dot = generate_dot_graph("Árbol Binario", nodes, edges, node_attrs, graph_attrs)
    return save_graph_image(dot, "binary_tree_graph")

def generate_binary_search_tree_graph(bst):
    """
    Genera un gráfico para un árbol binario de búsqueda.
    
    Args:
        bst: Objeto BinarySearchTree
        
    Returns:
        Ruta a la imagen generada
    """
    nodes = []
    edges = []
    
    # Función recursiva para recorrer el árbol
    def traverse(node, node_id=None):
        if node is None:
            return
        
        current_id = id(node)
        nodes.append({
            'id': current_id,
            'label': f"Valor: {node.data}"
        })
        
        # Si es llamada desde un nodo padre, agregar la conexión
        if node_id is not None:
            edges.append({
                'from': node_id,
                'to': current_id,
                'label': "izq" if node.data < node.parent.data else "der"
            })
        
        # Recorrer hijos
        if node.left:
            traverse(node.left, current_id)
        
        if node.right:
            traverse(node.right, current_id)
    
    # Iniciar recorrido desde la raíz
    if bst.root:
        traverse(bst.root)
    
    # Si el árbol está vacío, mostrar un nodo vacío
    if not nodes:
        nodes.append({
            'id': 0,
            'label': "Árbol vacío"
        })
    
    # Marcar la raíz
    graph_attrs = {'rankdir': 'TB'}  # Orientación de arriba a abajo
    node_attrs = {}
    
    if bst.root and nodes:
        root_id = id(bst.root)
        node_attrs[root_id] = {'fillcolor': 'lightgreen', 'label': f"{nodes[0]['label']}\n(Raíz)"}
    
    dot = generate_dot_graph("Árbol Binario de Búsqueda", nodes, edges, node_attrs, graph_attrs)
    return save_graph_image(dot, "bst_graph") 