# Квадратура круга

# Напишите программу, которая запрашивает у пользователя радиус круга (вещественное число), вычисляет его площадь и выводит результат.
# Для преобразования ввода используйте функцию float(). Формула для вычисления площади круга: 𝜋*r^2 (π≈3.14)
# Пример:
# Введите радиус круга: 5
# Площадь круга: 78.5

# Напишите тут ваш код
Pi = 3.14
radius = float(input("Введите радиус круга: "))
s = Pi*radius**2
print(f"Площадь круга: {s}")