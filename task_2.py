print('Задача 2. Финансовый отчёт')

# Васе пришло очередное задание — автоматизация финансовой отчётности.
# Звучит сложно, а на деле нужно просто написать код, который будет считать нужные для отчёта вычисления автоматически.
# Вычисления, которые нужно реализовать в программе: сумму дохода первых двух кварталов поделить на сумму последних двух кварталов,
# чтобы понять динамику роста или падения дохода.

# Алгоритм действий в программе:
# 1) Запросить у пользователя четыре числа.
# 2) Отдельно сложить два первых и два вторых.
# 3) Разделить первую сумму на вторую.
# 4) Вывести результат на экран.

quarter_1, quarter_2, quarter_3, quarter_4 = ('', ) * 4

while quarter_1.strip() == '':
  quarter_1 = input('Введите сумму за первый квартал: ')
while quarter_2.strip() == '':
  quarter_2 = input('Введите сумму за второй квартал: ')
while quarter_3.strip() == '':
  quarter_3 = input('Введите сумму за третий квартал: ')
while quarter_4.strip() == '':
  quarter_4 = input('Введите сумму за четвертый квартал: ')
print('')

first_half_sum = int(quarter_1) + int(quarter_2)
second_half_sum = int(quarter_3) + int(quarter_4)

if first_half_sum == second_half_sum:
  print('Динамика за год нулевая.')
else:
  res = second_half_sum / first_half_sum
  res = float('{:.2f}'.format(res))
  if res > 1:
    res *= 100
    print(
      'Динамика за год увеличивается! Прирост к первому полугодию составил: ',
      res, '%.')
  else:
    res = 100 - res * 100
    print('Динамика за год уменьшается! Падение составило: ', res, '%.')

#Почему не завершается код - остается перманентно запущенным?

exit()
