# (c) 2025 Flarosoft Development.
# Github Repository: https://github.com/flarosoftdev/Telegram-Mesage-Sender.git
# Telegram Channel with Flarosoft Bots: https://t.me/FlarosoftBots

__author__ = "Flarosoft"
__version__ = "0.1"
__author_email__ = "flarosoft.dev@gmail.com"

import sys
import telebot
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import requests
from io import BytesIO

TOKEN = "YOUR_BOT_TOKEN" # Замените на свой токен. Токен можно узнать, создав Telegram-бота с помощью @BotFather
bot = telebot.TeleBot(TOKEN)

class TelegramUserInfoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Telegram Message Sender")
        self.setGeometry(100, 100, 400, 500)
        self.setFixedSize(400, 500)

        self.token_label = QLabel("Введите токен бота:")
        self.token_input = QLineEdit(self)
        self.token_input.setText(TOKEN)
        self.token_button = QPushButton("Установить токен", self)
        self.token_button.clicked.connect(self.set_token)

        self.label = QLabel("Введите ID пользователя:")
        self.input_id = QLineEdit(self)
        self.button = QPushButton("Получить информацию", self)
        self.button.clicked.connect(self.fetch_user_info)
        
        self.result_label = QTextEdit(self)
        self.result_label.setReadOnly(True)
        self.avatar_label = QLabel(self)
        self.avatar_label.setAlignment(Qt.AlignCenter)
        
        self.msg_label = QLabel("Введите сообщение:")
        self.input_msg = QTextEdit(self)
        self.send_button = QPushButton("Отправить сообщение", self)
        self.send_button.clicked.connect(self.send_message)
        
        layout = QVBoxLayout()
        layout.addWidget(self.token_label)
        layout.addWidget(self.token_input)
        layout.addWidget(self.token_button)
        layout.addWidget(self.label)
        layout.addWidget(self.input_id)
        layout.addWidget(self.button)
        layout.addWidget(self.avatar_label)
        layout.addWidget(self.result_label)
        layout.addWidget(self.msg_label)
        layout.addWidget(self.input_msg)
        layout.addWidget(self.send_button)
        
        self.setLayout(layout)

    def set_token(self):
        global TOKEN, bot
        new_token = self.token_input.text().strip()
        if new_token:
            TOKEN = new_token
            bot = telebot.TeleBot(TOKEN)
            self.result_label.setText("Токен успешно установлен!")
        else:
            self.result_label.setText("Ошибка: введите токен!")

    def fetch_user_info(self):
        user_id = self.input_id.text().strip()
        if not user_id.isdigit():
            self.result_label.setText("Ошибка: введите числовой ID!")
            return
        self.get_user_info(user_id)
    
    def get_user_info(self, user_id):
        try:
            user = bot.get_chat(user_id)
            info = (
                f"Профиль пользователя:\n"
                f"ID: {user.id}\n"
                f"Имя: {user.first_name}\n"
                f"Фамилия: {user.last_name or 'Нет'}\n"
                f"Имя пользователя: {'@' + user.username if user.username else 'Нет'}\n"
                f"Описание: {user.bio if hasattr(user, 'bio') else 'Нет'}"
            )
            self.result_label.setText(info)
            
            if user.photo:
                file_id = user.photo.big_file_id
                file_info = bot.get_file(file_id)
                file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}"
                response = requests.get(file_url)
                pixmap = QPixmap()
                pixmap.loadFromData(BytesIO(response.content).read())
                self.avatar_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
            else:
                self.avatar_label.clear()
        except Exception as e:
            self.result_label.setText(f"Ошибка: {e}")
    
    def send_message(self):
        user_id = self.input_id.text().strip()
        message = self.input_msg.toPlainText().strip()
        if not user_id.isdigit():
            self.result_label.setText("Ошибка: введите числовой ID!")
            return
        if not message:
            self.result_label.setText("Ошибка: введите сообщение!")
            return
        try:
            bot.send_message(user_id, message)
            self.result_label.setText("Сообщение отправлено!")
        except Exception as e:
            self.result_label.setText(f"Ошибка при отправке: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelegramUserInfoApp()
    window.show()
    sys.exit(app.exec_())

