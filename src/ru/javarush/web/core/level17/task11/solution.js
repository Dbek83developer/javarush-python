// Запрашиваем возраст пользователя
const stringAge = prompt("Введите ваш возраст");
const age = parseInt(stringAge);

// Запрашиваем наличие водительских прав
const stringLicense = prompt("У вас есть водительские права? (yes или no)");
const hasLicense = stringLicense.toLowerCase() === 'yes';

// Проверяем условия и выводим соответствующее сообщение
if (age >= 18 && hasLicense) {
  console.log("Вы можете водить машину");
} else {
  console.log("Вам нельзя водить машину");
}