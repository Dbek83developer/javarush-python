function showItems(firstItem, ...restItems) {
    console.log(firstItem);
    console.log(restItems);
}

// Примеры вызова функции с различным количеством аргументов
showItems("яблоко", "банан", "груша");
showItems("машина");
showItems("первый", "второй", "третий", "четвертый");