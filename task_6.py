print('Задача 6. Проверяем бухгалтера')

# Реализуйте программу,
# которая запрашивает два числа у пользователя.
# После этого у каждого числа возьмите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.

# Пример:
# Введите первое число: 456
# Введите второе число: 123
# Сумма: 79

first_digit, second_digit = ('', ) * 2

print('')
while first_digit.strip() == '' or len(first_digit) < 2:
  first_digit = input('Введите первое число (не менее 2 знаков): ')
while second_digit.strip() == '' or len(first_digit) < 2:
  second_digit = input('Введите второе число (не менее 2 знаков): ')
print('')

#Первое решение:
print('Сумма:', int(first_digit) % 100 + int(second_digit) % 100)

#Второе решение:
#print('Сумма:', int(first_digit[-2:]) + int(second_digit[-2:]))

exit()
