# Telegram Message Sender

## Description
**Telegram Message Sender** is a desktop application on PyQt5 with a Russian interface for working with Telegram bots. It allows you to get information about Telegram users and send them messages using the Telegram Bot API.

## Features
- Setting up a bot token to work with Telegram API
- Getting user information by ID (name, last name, username, description)
- Displaying user avatar (if available)
- Sending messages to Telegram users

## Requirements
- Python 3.7+
- PyQt5
- Telebot
- Requests

## Installation and launch
1. Clone the repository:
```sh
git clone https://github.com/flarosoftdev/Telegram-Mesage-Sender.git
cd Telegram-Mesage-Sender
```
2. Install dependencies:
```sh
pip install -r requirements.txt
```
3. Run the application:
```sh
python telegram_messgae_sender.py
```

## Usage
1. Enter the bot token (you can get it from [@BotFather](https://t.me/BotFather))
2. Enter the user ID you want to get information about
3. Click "Get info" to see profile data
4. Enter the message text and click "Send message"

## Note
- **Do not pass the bot token to third parties!**
- **You can find out the user ID through the bot, for example, using the `/start` command and processing messages.**

## Contacts
- Developer: **Flarosoft**
- Email: [flarosoft.dev@gmail.com](mailto:flarosoft.dev@gmail.com)
- Developer's Telegram channel: [@flarosoftdev](https://t.me/flarosoftdev)
- Archive with Telegram bots from Flarosoft: [@flarosoftbots](https://t.me/flarosoftbots)
- GitHub: [Flarosoft Development](https://github.com/flarosoftdev)
