const employee = {
  firstName: 'John',
  lastName: 'Doe',
  position: 'Developer',
  salary: 50000
};

const { firstName: fName, lastName: lName } = employee;

console.log(fName);
console.log(lName);