// Запрашиваем число n у пользователя
const string = prompt("Введите число n:");
let n = parseInt(string);

// Инициализируем переменные
let sum = 0;
let i = 1;

// Используем цикл while для нахождения суммы всех чисел от 1 до n
while (i <= n) {
    sum += i;
    i++;
}


// Выводим результат на экран
console.log("Сумма чисел от 1 до " + n + " равна " + sum);