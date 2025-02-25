// Объявляем объект animal с методом speak
const animal = {
  speak() {
    console.log("Animal speaks");
  }
};

// Создаем объект dog, который наследует от animal
const dog = Object.create(animal);

// Переопределяем метод speak в объекте dog
dog.speak = function() {
  console.log("Dog barks");
};

// Вызов метода speak у объекта animal
animal.speak(); // Animal speaks

// Вызов метода speak у объекта dog
dog.speak(); // Dog barks