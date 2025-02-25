Array.prototype.sum = function() {
  return this.reduce((acc, val) => acc + val, 0);
};

const numbers = [1, 2, 3, 4, 5];
console.log(numbers.sum()); // 15