// Запрашиваем у пользователя, является ли сегодня выходным
const stringWeekend = prompt("Сегодня выходной? (yes/no)");
let isWeekend = stringWeekend === 'yes';

// Запрашиваем у пользователя, является ли сегодня праздничным днем
const stringHoliday = prompt("Сегодня праздничный день? (yes/no)");
let isHoliday = stringHoliday === 'yes';

// Проверяем условия и выводим соответствующее сообщение
if (isWeekend || isHoliday) {
    console.log("Сегодня выходной");
} else {
    console.log("Сегодня рабочий день");
}