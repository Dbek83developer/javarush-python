# Снежинка Коха

# Напишите рекурсивный алгоритм для рисования снежинки Коха.
# Алгоритм должен использовать библиотеку turtle для рисования фрактальной кривой.

import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)
        t.right(120)
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)


def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


screen = turtle.Screen()
screen.bgcolor("sky blue")
t = turtle.Turtle()
t.speed(0)
t.color("white")

# Рисуем снежинку
t.penup()
t.goto(-100, 50)
t.pendown()

order = 3  # глубина фрактала
size = 300  # Сторона

koch_snowflake(t, order, size)

t.hideturtle()
screen.mainloop()