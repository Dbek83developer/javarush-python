function setAndGetDateComponents() {
    // Создаем объект Date
    let date = new Date();
    
    // Устанавливаем дату 15 января 2025 года
    // Январь - это 0, так как месяцы нумеруются с 0
    date.setFullYear(2025);
    date.setMonth(0); // Январь - это 0, так как месяцы нумеруются с 0
    date.setDate(15);

    // Устанавливаем время 12:30:45
    date.setHours(12);
    date.setMinutes(30);
    date.setSeconds(45);
    
    // Возвращаем объект с компонентами даты
    return {
        year: date.getFullYear(),
        month: date.getMonth(), // Январь - это 0
        day: date.getDate(),
        hours: date.getHours(),
        minutes: date.getMinutes(),
        seconds: date.getSeconds()
    };
}