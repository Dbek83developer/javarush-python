//Создание объекта
const product = {
    name: "Sample Product",
    price: 29.99,
};

//Добавление метода
product.getProductInfo = function () {
    return `Product: ${this.name}, Price: $${this.price}`;
}

//Вызов метода
console.log(product.getProductInfo());