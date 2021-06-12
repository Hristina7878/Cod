number_1 = int(input('Введите первое число: '))
operation = input('Введите операцию: ')
number_2 = int(input('Введите второе число: '))
if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)
elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)
elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)
elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)
else:
    print('Вы не ввели действительный оператор, пожалуйста, запустите программу еще раз')
