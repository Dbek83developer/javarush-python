// Объявление массива colors
const colors = ['red', 'green', 'blue', 'yellow'];

// Деструктуризация массива для извлечения первого и третьего элементов
const [firstColor, , thirdColor] = colors;

// Вывод значений переменных firstColor и thirdColor в консоль
console.log(firstColor); // red
console.log(thirdColor); // blue