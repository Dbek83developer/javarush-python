# Google Cloud Vision API

# Напишите программу, которая использует Google Cloud Vision API для анализа изображения и распознавания объектов.
from google.cloud import vision
import io

# Инициализация клиента
client = vision.ImageAnnotatorClient()

# Загрузка изображения
file_name = 'class.jpg'
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Обнаружение объектов
response = client.object_localization(image=image)
objects = response.localized_object_annotations

# Вывод обнаруженных объектов
for object_ in objects:
    print(f'Object name: {object_.name}')
    print(f'Score: {object_.score}')