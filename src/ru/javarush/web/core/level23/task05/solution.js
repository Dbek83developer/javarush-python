// Объявление Set для хранения уникальных email адресов
const emailSet = new Set();

// Добавление email адресов, включая дублирующиеся
emailSet.add('example1@example.com');
emailSet.add('example2@example.com');
emailSet.add('example3@example.com');
emailSet.add('example2@example.com'); // дублирующийся email

// Проверка наличия одного из email
console.log(emailSet.has('example2@example.com')); // должно вывести true

// Удаление одного из email
emailSet.delete('example1@example.com');

// Вывод всех уникальных email адресов с использованием цикла for...of
for (const email of emailSet) {
  console.log(email);
}

// Очистка Set, удаление всех email адресов
emailSet.clear();