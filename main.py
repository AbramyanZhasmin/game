import random

name = 'Жасмин'
guesser = 0

number = random.randint(1, 30)
print('Отлично, ' + name + ' я загадал число между 1 и 30. Сможешь угадать?')
while guesser < 6:

    guess = int(input('Введи число: '))

    guesser += 1

    if guess < number:
        print('Твое число меньше того, что я загадал.')

    if guess > number:
        print('Твое число больше загаданного мной.')

    if guess == number:
        break

if guess == number:
    print('Ух ты, Ты угадал мое число)')
else:
    print('А вот и не угадал! Я загадал число {0}')
