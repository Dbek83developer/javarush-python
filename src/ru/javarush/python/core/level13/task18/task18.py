# OpenWeatherMap API

# Напишите программу, которая использует OpenWeatherMap API для получения текущей погоды в указанном городе.
import requests
API_KEY = '6c4e3098ecbbd2d3c1fd8033fe3dcc95'
city = input("Enter the city: ")
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
response = requests.get(url)
data = response.json()
if response.status_code == 200:
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    print(f'Погода в {city}: {weather}, температура: {temp}°C')
else:
    print('Ошибка получения данных о погоде')