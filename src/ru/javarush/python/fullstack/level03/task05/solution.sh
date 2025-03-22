# Сборка Docker образа:
docker build -t my-node-app .

# Запуск контейнера:
docker run -d -p 4000:4000 my-node-app