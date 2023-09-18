import sympy as sp

def bisection_method(equation_str, a, b, tol=1e-6, max_iter=100):
    x = sp.Symbol('x')
    func = sp.sympify(equation_str)

    if func.subs(x, a) * func.subs(x, b) >= 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала [a, b].")

    iteration = 0
    while (b - a) / 2.0 > tol and iteration < max_iter:
        c = (a + b) / 2.0
        if func.subs(x, c) == 0:
            return c  # Найден точный корень
        elif func.subs(x, c) * func.subs(x, a) < 0:
            b = c
        else:
            a = c
        iteration += 1

    # Возвращаем приближенное значение корня и количество итераций
    return (a + b) / 2.0, iteration

# Пример использования:
if __name__ == "__main__":
    equation_str = input("Введите уравнение (используйте 'x' в качестве переменной): ")
    a = float(input("Введите начало интервала a: "))
    b = float(input("Введите конец интервала b: "))
    tolerance = 1e-6
    max_iterations = 100

    root, iterations = bisection_method(equation_str, a, b, tol=tolerance, max_iter=max_iterations)
    print(f"Приближенное значение корня: {root}")
    print(f"Количество итераций: {iterations}")
