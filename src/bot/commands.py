from aiogram import types
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot import kb
from bot import text

router = Router()


@router.message(CommandStart())
async def start_handler(msg: types.Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)
