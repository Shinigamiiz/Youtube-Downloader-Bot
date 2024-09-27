from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Что мне делать?")]], resize_keyboard=True)


chBtn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="720", callback_data="720")],
    [InlineKeyboardButton(text="360", callback_data="360")],
    [InlineKeyboardButton(text="🎧", callback_data="mp3")],
    [InlineKeyboardButton(text="🖼️", callback_data="jpg")],
])
