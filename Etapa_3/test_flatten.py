import unittest
from flatten import flatten

class TestFlatten(unittest.TestCase):

    def test_lista_simple(self):
        self.assertEqual(flatten([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_lista_anidada(self):
        self.assertEqual(flatten([1, [2, 3], [4, [5, 6]]]), [1, 2, 3, 4, 5, 6])

    def test_estructuras_diferentes(self):
        entrada = [1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]
        resultado_esperado = [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8]
        self.assertEqual(flatten(entrada), resultado_esperado)

    def test_elementos_vacios(self):
        self.assertEqual(flatten([]), [])
        self.assertEqual(flatten([[], (), {}, [[], {}]]), [])

if __name__ == '__main__':
    unittest.main()
