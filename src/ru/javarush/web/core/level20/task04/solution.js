// Создаем объект organism с методом live
const organism = {
  live() {
    console.log("Living");
  }
};

// Создаем объект animal с методом move и устанавливаем его прототипом organism
const animal = Object.create(organism);
animal.move = function() {
  console.log("Moving");
};

// Создаем объект bird с методом fly и устанавливаем его прототипом animal
const bird = Object.create(animal);
bird.fly = function() {
  console.log("Flying");
};

// Вызываем методы live, move и fly у объекта bird
bird.live(); // Living
bird.move(); // Moving
bird.fly();  // Flying