function updateTime() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const formattedTime = `${hours}:${minutes}`;

    const clockElement = document.getElementById('clock');
    if (clockElement) {
        clockElement.textContent = formattedTime;
    }
}

function startClock() {
    setInterval(updateTime, 1000);
    updateTime(); // Update immediately without waiting 1 second
}