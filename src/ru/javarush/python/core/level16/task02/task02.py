# Поиск это легко

# Напишите функцию, которая выполняет линейный поиск для проверки наличия заданного элемента в списке строк.
# Функция должна возвращать True, если элемент найден, и False, если элемент отсутствует.
# Пользоваться классом list можно, вызывать его функции - нет.

def find_string(spisok, word):
    # print(len(spisok))
    for i in range(len(spisok)):
        if spisok[i] == word:
            return True
    return False


data = ['aAA', 'dddd', 's', 'sss']
print(find_string(data, 'dddd'))