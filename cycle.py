steps = 0

    # очевидно, что влево и вниз, шагать нельзя,
    # так как координаты будут 999, и сумма уже больше 25.
    # Проходим по диапазону до условных 2000, т.к. 1999 точно нельзя наступать.

x=6473
a = x // 1000 % 10
b = x // 100 % 10
c = x // 10 % 10
d = x % 10
sumX = a+b+c+d
print(a, b, c, d, a+b+c+d)

for x in range (1000, 2000):
        # Находим сумму цифр первой координаты
    a = x // 1000 % 10
    b = x // 100 % 10
    c = x // 10 % 10
    d = x % 10
    sumX = a+b+c+d
        # Если сумма цифр координаты X равна 25, останавливаем цикл, т.к. + 1000(1) по Y =26
    if sumX >= 25:
        break

        # Аналогично для каждого X Пробегаем по диапазону
    for y in range (1000, 2000):
            # Находим сумму цифр первой координаты
        e = y // 1000 % 10
        f = y // 100 % 10
        g = y // 10 % 10
        h = y % 10
        sumY = e+f+g+h
            # Если условие работает, добавляем кол-во шагов
        if sumX + sumY <= 25:
            steps += 1
            # Иначе останавливаем цикл
        else:
            break
print("Количество доступных клеток =", steps)

