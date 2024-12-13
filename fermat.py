def fermat_theorem(a, b, c, n):
    """
    Проверяет теорему Ферма для заданных a, b, c и n.
    
    :param a: Первое целое число
    :param b: Второе целое число
    :param c: Третье целое число
    :param n: Степень (должна быть больше 2)
    :return: True если теорема выполняется (что неправильно), иначе False
    """
    if n <= 2:
        raise ValueError("Степень n должна быть больше 2")
    
    return a**n + b**n == c**n