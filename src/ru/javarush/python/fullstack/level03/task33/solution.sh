# Сборка Docker-образа с вашим именем пользователя Docker Hub:
docker build -t dbek/my-python-app:1.0 .

# Авторизация в Docker Hub:
docker login

# Публикация образа в Docker Hub:
docker push dbek/my-python-app:1.0
