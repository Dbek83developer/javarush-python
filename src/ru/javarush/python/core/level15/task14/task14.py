# Люблю список еще больше

# Напишите программу, которая создает динамический массив (список)
# и демонстрирует его основные операции: добавление, удаление, доступ по индексу и изменение элемента.
# Класс list использовать нельзя.

class DynamicArray:
    def __init__(self):
        self.array = []

    def add(self, element):
        self.array.append(element)


    def remove(self, index):
        if self.__len__() != 0 and self.__len__() > index:
            self.array.pop(index)
        else:
            print("Empty array")


    def get(self, index):
        if self.__len__() != 0 and self.__len__() > index:
            return self.array[index]
        else:
            print("IndexOut of bond")

    def set(self, index, element):
        if self.__len__() > index:
            self.array[index] = element
        else:
            raise Exception("IndexOut of bond")



    def __len__(self):
        return len(self.array)

    def __str__(self):
        return str(self.array)


# Примеры использования:
arr = DynamicArray()
arr.add(1)
arr.add(2)
arr.add(3)
print(arr)  # [1, 2, 3]

arr.remove(2)
print(arr)  # [1, 2]

print(arr.get(1))  # 2

arr.set(1, 5)
print(arr)  # [1, 5]

print(len(arr))  # 2