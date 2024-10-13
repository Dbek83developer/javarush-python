# Использование энкодера

# Напишите программу, которая сериализует объект Python, содержащий дату и время, в JSON-строку
# с использованием пользовательского кодера для преобразования объектов datetime в строковый формат ISO.

import json
from datetime import datetime


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


data = {
    "name": "Alice",
    "timestamp": datetime.now()
}

# Сериализация с пользовательским кодером
json_string = json.dumps(data, cls=CustomEncoder, indent=4)
print(json_string)
