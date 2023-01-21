ticket = input("Введите количество приобретаемых билетов: ")
if not ticket or not ticket.isdigit():
    print("Вы не указали количество или ввели недопустимое значение")
else:
    ticket = int(ticket)
    person, sum = ticket, 0
    while person >= 1:
        age = input(f'Укажите возраст посетителя № {person} ? ')
        if not age or not age.isdigit() or int(age) > 129:
            print("Вы не указали возраст или ввели недопустимое значение")
        else:
            age = int(age)
            if age < 18:
                print('Билет бесплатный')
            elif 25 > age >= 18:
                sum += 990
                print('Стоимость билета: 990 руб.')
            elif age >= 25:
                sum += 1390
                print('Стоимость билета: 1390 руб.')
            person -= 1
    if ticket > 3:
        sale = int(sum - ((sum / 100) * 10))
        print(f'К оплате {sale} руб., активирована скидка 10% за покупку более 3ёх билетов')
    else:
        print(f'К оплате {sum} руб.')
