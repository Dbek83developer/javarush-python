async function delayedMessage(message, delay) {
  await new Promise(resolve => setTimeout(resolve, delay));
  return message;
}

// Демонстрация работы функции
(async () => {
  const result = await delayedMessage("Hello, World!", 2000);
  console.log(result); // Сообщение будет выведено в консоль через 2 секунды
})();