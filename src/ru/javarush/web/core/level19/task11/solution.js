function createCounter() {
  let count = 0;
  return function() {
    count += 1;
    return count;
  };
}

// Создание двух независимых счетчиков
const counter1 = createCounter();
const counter2 = createCounter();

// Демонстрация работы первого счетчика
console.log(counter1()); // 1
console.log(counter1()); // 2
console.log(counter1()); // 3

// Демонстрация работы второго счетчика
console.log(counter2()); // 1
console.log(counter2()); // 2
console.log(counter2()); // 3