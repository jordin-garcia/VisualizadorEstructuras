from enum import Enum

class DataType(Enum):
    INTEGER = "Entero"
    FLOAT = "Flotante"
    BOOLEAN = "Booleano"
    STRING = "Cadena"
    OBJECT = "Objeto"

def validate_data(data, data_type):
    """
    Valida que el dato sea del tipo especificado.
    
    Args:
        data: El dato a validar
        data_type: Tipo de dato esperado (DataType)
    
    Returns:
        bool: True si el dato es válido, False en caso contrario
    """
    try:
        if data_type == DataType.INTEGER:
            int(data)
            return True
        elif data_type == DataType.FLOAT:
            float(data)
            return True
        elif data_type == DataType.BOOLEAN:
            return data.lower() in ["true", "false", "verdadero", "falso", "1", "0"]
        elif data_type == DataType.STRING:
            return isinstance(data, str)
        elif data_type == DataType.OBJECT:
            # En el caso de objeto, aceptamos cualquier dato
            return True
        return False
    except (ValueError, TypeError):
        return False

def convert_data(data, data_type):
    """
    Convierte el dato al tipo especificado.
    
    Args:
        data: El dato a convertir
        data_type: Tipo de dato objetivo (DataType)
    
    Returns:
        El dato convertido al tipo especificado
    """
    if data_type == DataType.INTEGER:
        return int(data)
    elif data_type == DataType.FLOAT:
        return float(data)
    elif data_type == DataType.BOOLEAN:
        if data.lower() in ["true", "verdadero", "1"]:
            return True
        else:
            return False
    elif data_type == DataType.STRING:
        return str(data)
    elif data_type == DataType.OBJECT:
        # Para objetos, usamos la representación como string
        return data
    return data 