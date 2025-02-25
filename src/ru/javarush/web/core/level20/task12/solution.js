// Объявление класса Animal
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a noise.`);
  }
}

// Объявление класса Predator, наследующего Animal
class Predator extends Animal {
  hunt() {
    console.log(`${this.name} is hunting.`);
  }
}

// Создание экземпляра класса Predator
const predator = new Predator('Lion');

// Вызов методов speak и hunt для экземпляра класса Predator
predator.speak(); // Вывод: Lion makes a noise.
predator.hunt();  // Вывод: Lion is hunting.