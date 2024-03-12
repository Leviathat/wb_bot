from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Получить информацию по товару")],
        [KeyboardButton(text="Остановить уведомления")],
        [KeyboardButton(text="Получить информацию из БД")],
    ],
    resize_keyboard=True,
)

exit_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Главное меню")]
    ],
    resize_keyboard=True,
)

subscribe = [
    [InlineKeyboardButton(text="Подписаться",
                          callback_data="subscribe_card")],
]
