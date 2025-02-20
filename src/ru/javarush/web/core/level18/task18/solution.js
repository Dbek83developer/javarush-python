// Создание объекта person
const person = {
    name: 'John Doe',
    age: 30,
    email: 'john.doe@example.com',
    country: 'USA'
};

// Деструктуризация с оператором rest
const { name, age, ...restProperties } = person;

// Вывод объекта restProperties в консоль
console.log(restProperties);