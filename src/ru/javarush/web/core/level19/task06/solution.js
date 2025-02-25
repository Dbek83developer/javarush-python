function bold(strings, ...values) {
  return strings.reduce((result, str, i) => {
    return result + str + (values[i] !== undefined ? `<b>${values[i]}</b>` : '');
  }, '');
}

// Пример вызова функции
const name = "John";
const age = 30;
const result = bold`Name: ${name}, Age: ${age}`;

console.log(result);  // Вывод: Name: <b>John</b>, Age: <b>30</b>