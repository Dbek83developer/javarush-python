// Создаем объект machine с методом start
const machine = {
    start: function() {
        console.log("Machine started");
    }
};

// Создаем объект robot, который наследует от machine
const robot = Object.create(machine);

// Добавляем метод stop в прототип объекта machine
machine.__proto__.stop = function() {
    console.log("Machine stopped");
};

// Вызываем метод stop у объекта robot
robot.stop();