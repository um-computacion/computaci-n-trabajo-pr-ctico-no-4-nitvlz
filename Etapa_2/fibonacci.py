def fibonacci_iterative(n):
    """
    Calcula el enésimo número de Fibonacci de forma iterativa.

    Parámetros:
        n (int): Índice en la sucesión (n >= 0)

    Retorna:
        int: El valor de Fibonacci en la posición n.

    Lanza:
        ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_recursive(n):
    """
    Calcula el enésimo número de Fibonacci de forma recursiva.

    Parámetros:
        n (int): Índice en la sucesión (n >= 0)

    Retorna:
        int: El valor de Fibonacci en la posición n.

    Lanza:
        ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
