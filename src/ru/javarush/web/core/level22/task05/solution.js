function fetchData(value) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(value);
        }, 1000);
    });
}

fetchData(1)
    .then(result => {
        console.log(result);
        return fetchData(result * 2);
    })
    .then(result => {
        console.log(result);
        return fetchData(result * 3);
    })
    .then(result => {
        console.log(result);
        return fetchData(result * 4);
    })
    .then(finalResult => {
        console.log("Final Result:", finalResult);
    });