// Синхронная операция
console.log('1. Синхронный вывод');

// Асинхронная операция через Promise
Promise.resolve().then(() => {
  console.log('3. Promise.then');
});

// Синхронная операция
console.log('2. Синхронный вывод');

// Асинхронная операция через setTimeout
setTimeout(() => {
  console.log('4. setTimeout');
}, 0);