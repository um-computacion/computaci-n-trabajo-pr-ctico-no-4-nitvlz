def flatten(data):
    """
    Aplana cualquier estructura de datos anidada (listas, tuplas, diccionarios).

    Parámetros:
        data (list | tuple | dict | cualquier iterable): Estructura posiblemente anidada.

    Retorna:
        list: Lista aplanada con todos los elementos en orden.
    """
    result = []

    if isinstance(data, dict):
        for key, value in data.items():
            result.extend(flatten(key))
            result.extend(flatten(value))
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            result.extend(flatten(item))
    elif data is not None:
        result.append(data)

    return result

