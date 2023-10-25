print('Задача 4. Площадь треугольника')

# Напишите программу,
# которая запрашивает у пользователя длины двух катетов
# в прямоугольном треугольнике и выводит его площадь.

# Формула:
# S = ab/2

first_cathet, second_cathet = ('', ) * 2

print('')
while first_cathet.strip() == '':
  first_cathet = input('Введите длину первого катета: ')
while second_cathet.strip() == '':
  second_cathet = input('Введите длину второго катета: ')
print('')

square = (float(first_cathet) * float(second_cathet)) / 2
print('Площадь прямоугольного треугольника равна', square)

exit()