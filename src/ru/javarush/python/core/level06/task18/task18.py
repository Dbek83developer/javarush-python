# Символы в строке

# Напишите программу, которая принимает строку от пользователя, выводит ее длину,
# а затем запрашивает у пользователя индекс.
# Программа должна вывести символ строки по этому индексу.
# Если индекс выходит за пределы строки, программа должна вывести соответствующее сообщение.

# Напишите тут ваш код
try:
    str1 = input("enter text: ")
    print(len(str1))
    index = int(input("enter the index: "))
    print(str1[index])
except IndexError:
    print("IndexError index ne pravilniy")
