const user = {
    username: 'JohnDoe',
    email: 'johndoe@example.com',
    getDetails() {
        return `Username: ${this.username}, Email: ${this.email}`;
    }
};

console.log(user.getDetails());