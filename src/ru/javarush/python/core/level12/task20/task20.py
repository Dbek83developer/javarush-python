# Исключение несериализуемых полей

# Напишите класс, который содержит несериализуемые поля, такие как открытые файлы или базы данных,
# и реализуйте методы __getstate__() и __setstate__(),
# чтобы исключить эти поля при сериализации и восстановить их при десериализации.
import pickle


class MyClass:
    def __init__(self, filename):
        self.filename = filename
        # Открываем файл
        self.file = open(filename, 'w')
        # Псевдосоединение с базой данных (для примера)
        self.db_connection = self.connect_to_database()

    def connect_to_database(self):
        # Допустим, это подключение к базе данных
        return "Connection to database"

    def write_to_file(self, text):
        self.file.write(text)

    def close(self):
        self.file.close()
        # Закрываем псевдосоединение с базой данных
        self.db_connection = None

    def __getstate__(self):
        """
        Этот метод вызывается при сериализации.
        Мы должны удалить несериализуемые объекты, например, файлы и соединения.
        """
        state = self.__dict__.copy()
        # args = self.filename
        # Убираем несериализуемые поля
        state['file'] = None
        state['db_connection'] = None
        return state  # , args

    def __setstate__(self, state):
        """
        Этот метод вызывается при десериализации.
        Мы должны восстановить состояние объекта.
        """
        self.__dict__.update(state)
        # Файл и соединение с базой данных не восстанавливаются автоматически
        # Нужно заново открыть файл или восстановить соединение, если нужно
        if 'filename' in state:
            self.file = open(state['filename'], 'w')
        self.db_connection = self.connect_to_database()


# Пример использования
my_obj = MyClass('test.txt')
my_obj.write_to_file('Hello, world!')
my_obj.close()

# Попробуем сериализовать объект
serialized_data = pickle.dumps(my_obj)

# Попробуем десериализовать объект
deserialized_obj = pickle.loads(serialized_data)
print(deserialized_obj.db_connection)  # Псевдоподключение должно быть восстановлено
