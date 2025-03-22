def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Введіть число для обчислення факторіалу: "))

if n < 0:
    print("Факторіал не визначений для від'ємних чисел.")
else:
    print(f"Факторіал числа {n} дорівнює {factorial(n)}.")
