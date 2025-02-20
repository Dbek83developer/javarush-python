function calculatePrice(price, tax = price * 0.1) {
    return price + tax;
}
// Вызов функции с одним аргументом
console.log(calculatePrice(100)); // Ожидаемый результат: 110

// Вызов функции с двумя аргументами
console.log(calculatePrice(100, 20)); // Ожидаемый результат: 120