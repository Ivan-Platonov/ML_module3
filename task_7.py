print('Задача 7. Режем число на части')

# Реализуйте программу,
# которая получает на вход четырёхзначное число
# и выводит на экран каждую его цифру отдельно
# (в одну строчку либо каждая цифра в новой строчке).
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных

full_digit = ''

print('')
while full_digit == '' or len(full_digit) != 4:
  full_digit = input('Введите четырехзначное число: ')
print('')

int_full_digit = int(full_digit)

first_digit = int((int_full_digit - int_full_digit % 1000) / 1000)
second_digit = int((int_full_digit % 1000 - int_full_digit % 100) / 100)
third_digit = int((int_full_digit % 100 - int_full_digit % 10) / 10)
fourth_digit = (int_full_digit % 10)

#Первый вариант:
print('Число состоит из цифр:')
print(
  str(first_digit) + ',',
  str(second_digit) + ',',
  str(third_digit) + ',', 
  str(fourth_digit))

#Второй вариант:
#print('Число состоит из цифр:')
##print(full_digit[0], full_digit[1], full_digit[2], full_digit[3])

exit()
