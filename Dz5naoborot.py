salary, expenses = int(input('Введите зарплату - ')), int(input('Введите затраты - '))
nakopleniya = salary - expenses
for i in range(11):
    salary += salary * 0.03
    nakopleniya += salary - expenses
print(f'Сотрудник накопит: {"%.2f" % nakopleniya} рублей')