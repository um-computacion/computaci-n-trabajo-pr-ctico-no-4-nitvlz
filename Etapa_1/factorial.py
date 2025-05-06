def factorial_iterative(n):
    """
    Calcula el factorial de un número de forma iterativa.
    
    Parámetros:
        n (int): Número entero no negativo.

    Retorna:
        int: El factorial de n.

    Lanza:
        ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def factorial_recursive(n):
    """
    Calcula el factorial de un número de forma recursiva.

    Parámetros:
        n (int): Número entero no negativo.

    Retorna:
        int: El factorial de n.

    Lanza:
        ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)
