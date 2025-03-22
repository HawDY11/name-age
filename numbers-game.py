import random

numbers =  random.randint(1,10)

attempts = 3

print("Вітаю у грі Вгадай число!")
print("Я загадав число від 1 до 10. Ти маєш 3 спроби, щоб вгадати його.")

while attempts > 0:

    user_guess = int(input(f"У тебе залишилось {attempts} спроб. Введи число: "))
    
    if user_guess == numbers:
        print("Вітаємо! Ти вгадав число!")
        break
    elif user_guess > numbers:
        print("Менше!")
    else:
        print("Більше!")

    attempts -= 1

if attempts == 0 and user_guess != numbers:
    print(f"На жаль, ти не вгадав. Загадане число було {numbers}.")