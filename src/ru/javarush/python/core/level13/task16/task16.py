# Отправка почты с использованием SMTP

# Напишите программу, которая подключается к SMTP-серверу, аутентифицируется и отправляет письмо.
import smtplib

# Учётные данные для входа
username = 'dbeknpout@yandex.ru'
password = '56693280548da105524f8ea539a73b17'


# Учётные данные для входа
smtp_server = 'smtp.yandex.ru'
smtp_port = 465
# username = 'dbeknpout@yandex.ru'
# password = 'your_app_password'  # Используйте пароль приложения

# Адреса отправителя и получателя
from_addr = 'dbeknpout@yandex.ru'
to_addr = 'bahodir-d.b@mail.ru'

# Тема и тело письма
subject = 'Тема письма'
body = 'Это текст письма.'

# Формирование сообщения в формате строки
message = f"From: {from_addr}\nTo: {to_addr}\nSubject: {subject}\n\n{body}"

try:
    # Подключение к SMTP-серверу
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Защищённое соединение

    # Аутентификация
    server.login(username, password)

    # Отправка сообщения
    server.sendmail(from_addr, to_addr, message)
    print("Письмо успешно отправлено!")
except smtplib.SMTPConnectError:
    print("No connect")
except smtplib.SMTPAuthenticationError:
    print("Authentification error")
except Exception as e:
    print(f"Ошибка при отправке письма: {e}")
finally:
    # Закрытие соединения
    server.quit()
