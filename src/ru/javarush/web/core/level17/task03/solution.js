// Генерация случайных чисел и их округление
const randomA = Math.random() * 100; // Случайное число от 0 до 100
const randomB = Math.random() * 100; // Случайное число от 0 до 100

const intA = Math.round(randomA); // Округляем до ближайшего целого
const intB = Math.round(randomB); // Округляем до ближайшего целого

// Нахождение максимального и минимального значений
let maxNumber = Math.max(intA, intB);
let minNumber = Math.min(intA, intB);

// Вывод результатов
console.log('Сгенерированные числа:', randomA, randomB);
console.log('Максимальное значение:', maxNumber);
console.log('Минимальное значение:', minNumber);