from telebot import TeleBot
from settings import config
from handlers.handler_main import HandlerMain


class TelBot:

    """
        Основной класс телеграм бота (серва), в основе которога
        используется библиотека pyTelegramBotAPI
    """

    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self):

        self.token = config.TOKEN
        self.bot = TeleBot(self.token)
        self.handler = HandlerMain(self.bot)


    def start(self):
        """
            Метод предназначен для старта обрабоьчика событий
        :param self:
        :return:
        """

        self.handler.handle()

    def run_bot(self):

        """
            Метод запускает основные события сервера
        :param self:
        :return:
        """

        self.start()
        self.bot.polling(none_stop=True)


if __name__ == "__main__":
    bot = TelBot()
    bot.run_bot()