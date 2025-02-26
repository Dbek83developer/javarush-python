function loadResource(shouldFail = false) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (shouldFail) {
                reject('Ошибка при загрузке ресурса');
            } else {
                resolve('Ресурс успешно загружен');
            }
        }, 1000);
    });
}

loadResource()
    .then(result => {
        console.log(result);
        return loadResource(true);
    })
    .then(result => {
        console.log(result);
        return loadResource();
    })
    .then(result => {
        console.log(result);
    })
    .catch(error => {
        console.error('Произошла ошибка:', error);
    })
    .finally(() => {
        console.log('Завершение цепочки промисов');
    });