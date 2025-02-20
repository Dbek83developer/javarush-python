const book = {
  title: "To Kill a Mockingbird",
  author: "Harper Lee",
  year: 1960,
  getSummary: function() {
    return `${this.title} by ${this.author}, published in ${this.year}`;
  }
};

console.log(book.getSummary());