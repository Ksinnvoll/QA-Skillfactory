t = int(input("Введите количество билетов: "))
total = 0  # Общая сумма за билеты
cost = 0  # Стоимость одного билета
for i in range(t):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        cost = 0
        total += cost
    elif 18 <= age < 25:
        cost = 990
        total += cost
    elif age >= 25:
        cost = 1390
        total += cost
    if t > 3:
        total = round(total * 0.9, 1)  # Скидка 10% от общей суммы. Округление для привычного отображения суммы
print(f"Сумма к оплате составит: {total}")
