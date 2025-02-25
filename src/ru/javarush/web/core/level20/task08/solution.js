class User {
    constructor(username, email) {
        this.username = username;
        this.email = email;
    }

    getUsername() {
        return this.username;
    }

    getEmail() {
        return this.email;
    }
}

// Создание экземпляра класса User
const user = new User('john_doe', 'john@example.com');

// Вызов методов getUsername и getEmail
console.log(user.getUsername()); // Вывод: john_doe
console.log(user.getEmail());