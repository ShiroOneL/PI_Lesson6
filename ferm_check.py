def check_pythagorean(limit):
    print("Решения для n = 2:")
    for x in range(1, limit + 1):
        for y in range(x, limit + 1):  # y >= x
            z = (x**2 + y**2)**0.5
            if z.is_integer() and z <= limit:
                print(f"{x}^2 + {y}^2 = {int(z)}^2")

def check_fermat(n, limit):
    if n <= 2:
        print("n должно быть больше 2.")
        return

    print(f"Проверка для n = {n}:")
    found_solution = False
    for x in range(1, limit + 1):
        for y in range(x, limit + 1):  # y >= x
            for z in range(y, limit + 1):  # z >= y
                if x**n + y**n == z**n:
                    print(f"Найдены решения: {x}^{n} + {y}^{n} = {z}^{n}")
                    found_solution = True

    if not found_solution:
        print("Решений не найдено.")

# Пример использования
limit = 20  # верхний предел для x, y, z
check_pythagorean(limit)

n = 3  # степень для проверки
check_fermat(n, limit)

n = 4  # еще одна степень для проверки
check_fermat(n, limit)
