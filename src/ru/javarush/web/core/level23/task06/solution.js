// Создание объекта Map
const userRoles = new Map();

// Добавление пользователей и их ролей
userRoles.set('Alice', 'admin');
userRoles.set('Bob', 'editor');
userRoles.set('Charlie', 'viewer');

// Использование цикла for...of для перебора всех элементов в Map
for (const [user, role] of userRoles) {
  // Вывод пользователей и их ролей
  console.log(`${user}: ${role}`);
}