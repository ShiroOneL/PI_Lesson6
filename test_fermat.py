import unittest
from fermat import *

class TestFermatTheorem(unittest.TestCase):
    
    def test_fermat_valid(self):
        # Примеры, которые должны вернуть False (теорема выполняется)
        self.assertFalse(fermat_theorem(3, 4, 5, 5))  # 3^2 + 4^2 != 5^2
        self.assertFalse(fermat_theorem(1, 2, 3, 3))  # 1^3 + 2^3 != 3^3

    def test_fermat_invalid(self):
        # Примеры, которые должны вернуть True (теорема не выполняется)
        self.assertFalse(fermat_theorem(3, 4, 5, 3))   # 3^3 + 4^3 == 5^3 (неверно)

    def test_invalid_n(self):
        # Проверка на ошибку при n <= 2
        with self.assertRaises(ValueError):
            fermat_theorem(1, 1, 1, 2)
        with self.assertRaises(ValueError):
            fermat_theorem(1, 1, 1, 1)

if __name__ == '__main__':
    unittest.main()