# API от OpenAI

# Напишите программу, которая использует OpenAI API для получения ответа от модели ChatGPT.
import openai

# Ваш API-ключ OpenAI
api_key = 'YOUR_OPENAI_API_KEY'

# Аутентификация
openai.api_key = api_key

# Запрос к модели ChatGPT
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Расскажи мне интересный факт о космосе.",
    max_tokens=500
)

# Печать ответа
print(response.choices[0].text.strip())