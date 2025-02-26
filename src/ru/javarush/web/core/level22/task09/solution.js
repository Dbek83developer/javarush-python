// Подключение библиотеки Axios
const axios = require('axios');

// Определение функции fetchTodo
const fetchTodo = () => {
    axios.get('https://jsonplaceholder.typicode.com/todos/1')
        .then(response => {
            // Обработка успешного ответа
            console.log(response.data);
        })
        .catch(error => {
            // Обработка ошибок
            console.error('Ошибка при получении данных:', error.message);
        });
};

// Вызов функции
fetchTodo();