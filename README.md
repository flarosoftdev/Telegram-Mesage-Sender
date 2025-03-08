# Telegram Message Sender

## Описание
**Telegram Message Sender** — это десктопное приложение на PyQt5 для работы с Telegram-ботами. Оно позволяет получать информацию о пользователях Telegram и отправлять им сообщения с помощью API Telegram Bot.

## Возможности
- Установка токена бота для работы с Telegram API
- Получение информации о пользователе по его ID (имя, фамилия, username, описание)
- Отображение аватарки пользователя (если доступна)
- Отправка сообщений пользователям Telegram

## Требования
- Python 3.7+
- PyQt5
- Telebot
- Requests

## Установка и запуск
1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/flarosoftdev/Telegram-Mesage-Sender.git
   cd Telegram-Mesage-Sender
   ```
2. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   ```
3. Запустите приложение:
   ```sh
   python main.py
   ```

## Использование
1. Введите токен бота (получить можно у [@BotFather](https://t.me/BotFather))
2. Введите ID пользователя, информацию о котором хотите получить
3. Нажмите "Получить информацию", чтобы увидеть данные профиля
4. Введите текст сообщения и нажмите "Отправить сообщение"

## Примечание
- **Не передавайте токен бота третьим лицам!**
- **ID пользователя можно узнать через бота, например, используя команду `/start` и обработку сообщений.**

## Контакты
- Разработчик: **Flarosoft**
- Email: [flarosoft.dev@gmail.com](mailto:flarosoft.dev@gmail.com)
- Telegram-канал с ботами: [@FlarosoftBots](https://t.me/FlarosoftBots)
- GitHub: [Flarosoft Development](https://github.com/flarosoftdev)

