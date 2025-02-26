function maxOfArray(numbers) {
    return Math.max.apply(null, numbers);
}

// Тестирование функции
const testArray = [3, 5, 7, 2, 8];
console.log(maxOfArray(testArray)); // Вывод: