function runTimers() {
    // Таймер для вывода сообщения "Привет!" через 3 секунды
    setTimeout(() => {
        console.log("Привет!");
    }, 3000);

    // Интервальный таймер для вывода текущего времени каждую секунду
    let intervalId = setInterval(() => {
        let currentTime = new Date().toLocaleTimeString();
        console.log(currentTime);
    }, 1000);

    // Остановка интервального таймера через 10 секунд
    setTimeout(() => {
        clearInterval(intervalId);
    }, 10000);
}

// Запуск всех таймеров при выполнении функции
runTimers();