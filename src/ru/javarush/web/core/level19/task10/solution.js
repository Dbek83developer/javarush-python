function createGreeting(greeting) {
    return function(name) {
        console.log(`${greeting}, ${name}!`);
    };
}

// Пример использования:
const greetInEnglish = createGreeting("Hello");
greetInEnglish("Alice"); // Выведет: "Hello, Alice!"

const greetInSpanish = createGreeting("Hola");
greetInSpanish("Carlos"); // Выведет: "Hola, Carlos!"