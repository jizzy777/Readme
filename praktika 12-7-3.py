prcnt = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму депозита:"))
b1 = int(prcnt['ТКБ']*money/100)
b2 = int(prcnt['СКБ']*money/100)
b3 = int(prcnt['ВТБ']*money/100)
b4 = int(prcnt['СБЕР']*money/100)
dep = [b1, b2, b3, b4]
print(dep)
print("Максимальная сумма, которую вы можете заработать:", max(dep))