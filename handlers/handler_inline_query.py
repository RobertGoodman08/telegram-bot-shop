# импортируем класс родитель
from handlers.handler import Handler
# импортируем сообщения пользователю
from settings.message import MESSAGES


class HandlerInlineQuery(Handler):
    """
    Класс обрабатывает входящие текстовые
    сообщения от нажатия на инлайн кнопоки
    """

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_product(self, call, code):
        """
        обрабатывает входящие запросы на нажатие кнопок товара inline
        """
        # создаеь запись в БД по факту заказа
        self.BD._add_orders(1, code, 1)

        self.bot.answer_callback_query(
            call.id,
            MESSAGES['product_order'].format(
                self.BD.select_single_product_name(code),
                self.BD.select_single_product_title(code),
                self.BD.select_single_product_price(code),
                self.BD.select_single_product_quantity(code)),
            show_alert=True)

    def handle(self):
        # обработчик(декоратор) запросов от нажатия на кнопки товара.
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            code = call.data
            if code.isdigit():
                code = int(code)

            self.pressed_btn_product(call, code)
