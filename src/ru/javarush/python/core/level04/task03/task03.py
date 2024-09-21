# Мешанина

# Напишите программу, которая запрашивает у пользователя целое число, вещественное число и строку.
# Затем преобразуйте целое число в вещественное, вещественное число в строку, и строку в целое число (если это возможно).
# Выведите результаты преобразований и их типы.

# Напишите тут ваш код
num = int(input("enter the integer number: "))
fnum = float(num)
fl_num = float(input("enter the float number: "))
str_num = str(fl_num)
stroka = input("enter the string: ")
if type(int(stroka)) == int:
    int_num = int(stroka)
print(f"{fnum} {type(fnum)}, {str_num} {type(str_num)}, {int_num} {type(int_num)}")
