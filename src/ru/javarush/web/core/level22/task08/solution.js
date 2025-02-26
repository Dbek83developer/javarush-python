function loadResource1() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('Resource 1 Loaded');
        }, 2000);
    });
}

function loadResource2() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('Resource 2 Loaded');
        }, 3000);
    });
}

async function loadAllResources() {
    const results = await Promise.all([loadResource1(), loadResource2()]);
    console.log(results);
}

// Запуск функции для демонстрации
loadAllResources();