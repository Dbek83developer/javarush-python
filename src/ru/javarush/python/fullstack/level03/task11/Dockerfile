# Используем официальный образ Node.js версии 14 в качестве базового
FROM node:14

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл package.json в рабочую директорию
COPY package.json /app/package.json

# Копируем файл server.js в рабочую директорию
COPY server.js /app/server.js

# Устанавливаем зависимости, используя NPM
RUN npm install

# Определяем команду для запуска приложения
CMD ["node", "server.js"]