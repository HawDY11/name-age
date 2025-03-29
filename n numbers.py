def numbers(n):
    even_numbers = [i for i in range(n, 0, -1) if i % 2 == 0]
    print(" ".join(map(str, even_numbers)))

n = int(input("Введіть число n: "))
print(numbers(n))
