def main():
    try:
        start = int(input("Введіть перше число (з): "))
        end = int(input("Введіть друге число (по): "))
        
        if 5 <= start <= 10 and 5 <= end <= 10:
            numbers = list(range(start, end + 1))
            print(f"Числа від {start} до {end}: {numbers}")
        else:
            print("Числа повинні бути в межах від 5 до 10.")

main()
