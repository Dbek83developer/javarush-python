class User {
    constructor(username, email) {
        this.username = username;
        this.email = email;
    }

    static fromObject(obj) {
        return new User(obj.username, obj.email);
    }
}


// Демонстрация работы метода fromObject с тестовыми данными
const testObj = { username: 'john_doe', email: 'john.doe@example.com' };
const newUser = User.fromObject(testObj);

console.log(newUser); // User { username: 'john_doe', email: 'john.doe@example.com' }