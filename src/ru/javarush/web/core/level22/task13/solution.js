// Объявление асинхронной функции fetchDataAsync
async function fetchDataAsync() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            // Имитация успешного выполнения или ошибки
            if (Math.random() > 0.5) {
                resolve({ id: 1, name: 'John Doe' });
            } else {
                reject(new Error('Failed to fetch data'));
            }
        }, 1000);
    });
}

// Объявление асинхронной функции loadDataAsync
async function loadDataAsync() {
    try {
        // Вызов функции fetchDataAsync и ожидание результата
        const data = await fetchDataAsync();
        // Вывод данных в консоль при успешном выполнении
        console.log(data);
    } catch (error) {
        // Вывод сообщения об ошибке в консоль при неудачном выполнении
        console.error(error);
    }
}

// Вызов функции loadDataAsync для тестирования
loadDataAsync();