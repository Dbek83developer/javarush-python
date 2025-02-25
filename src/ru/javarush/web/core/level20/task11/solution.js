class Employee {
    constructor(name, salary) {
        this.name = name;
        this.salary = salary;
    }
}

class Manager extends Employee {
    constructor(name, salary, department) {
        super(name, salary);
        this.department = department;
    }
}


// Создание экземпляра класса Employee
const employee = new Employee("John Doe", 50000);
console.log(`Employee Name: ${employee.name}, Salary: ${employee.salary}`);

// Создание экземпляра класса Manager
const manager = new Manager("Jane Doe", 70000, "Sales");
console.log(`Manager Name: ${manager.name}, Salary: ${manager.salary}, Department: ${manager.department}`);