// Конструктор Animal
function Animal(name, species) {
    this.name = name;
    this.species = species;
}

// Конструктор Dog, который наследует свойства от Animal с использованием call
function Dog(name, species) {
    Animal.call(this, name, species);
}

// Добавление метода bark в конструктор Dog
Dog.prototype.bark = function() {
    console.log(`Woof! I'm ${this.name}, the ${this.species}`);
};

// Создание экземпляра Dog
const myDog = new Dog('Buddy', 'dog');

// Проверка работы метода bark
myDog.bark(); // Вывод: "Woof! I'm Buddy, the dog"