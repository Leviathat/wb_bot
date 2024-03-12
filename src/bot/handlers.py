from aiogram import types, F
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.services import CardService
from bot import kb
from bot import text


router = Router()


def get_service() -> CardService:
    return CardService()


service = get_service()


@router.message(F.text == "Главное меню")
async def menu(msg: types.Message):
    await msg.answer(text.menu, reply_markup=kb.menu)


# Получить информацию по товару
@router.callback_query(F.data == "Получить информацию по товару")
async def input_id(clbck: types.CallbackQuery):
    await clbck.message.answer(text.gen_text, reply_markup=kb.exit_menu)


@router.message(F.text)
async def get_card(msg: types.Message):
    card_data = await service.get_card(int(msg.text))
    await msg.answer(card_data, reply_markup=kb.menu)
