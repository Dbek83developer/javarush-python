const user = {
  имя: "Alice",
  возраст: 25,
  профессия: "Engineer"
};

for (const key in user) {
  console.log(`${key}: ${user[key]}`);
}