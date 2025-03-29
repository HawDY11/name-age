def calculator():
    try:
        a = float(input("Введіть число (a): "))
        b = float(input("Введіть число (b): "))

        op = input("Введіть математичну операцію (+, -, *, /): ")

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                print("Ділення на нуль неможливе !")
                return
            result = a / b
        else:
            print("Невідома операція!")
            return

        print(f"Результат: {result}")

    except ValueError:
        print("Будь ласка, введіть правильні числа.")

# Запуск калькулятора
calculator()
