import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import texts_14_4
from config_14_4 import *
from keyboards_14_4 import *
from crud_functions import get_all_products

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
database = Dispatcher(bot, storage=MemoryStorage())



@database.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'ДОбро пожаловать {message.from_user.username}' + texts_14_4.start, reply_markup=start_kb)

@database.message_handler(text='О нас')
async def price(message):
    await message.answer(texts_14_4.abaut, reply_markup=start_kb)


@database.message_handler(text='Купить')
async def get_buying_list(message):
    db_file = 'database.db'
    products = get_all_products(db_file)
    for i, product in enumerate(products):
        title, description, price = product
        imag_pr = texts_14_4.image_product[i]
        with open(imag_pr, 'rb') as img:
            await message.answer(f'Название: {title}| \nОписание: {description}| \nЦена: {price}', )
            await message.answer_photo(img, )
    await message.answer('Выберите продукт для покупки: ', reply_markup=catalog_kb)

@database.callback_query_handler(text='buy_jamCh')
async def buy_l(call):
    await call.message.answer(text='Выберите объем', reply_markup=buyJam1)
    await call.answer()

@database.callback_query_handler(text='buy_jamCh1')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@database.callback_query_handler(text='buy_jamCh2')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@database.callback_query_handler(text='buy_jamCh3')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@database.callback_query_handler(text='buy_jamV')
async def buy_l(call):
    await call.message.answer(text='Выберите объем', reply_markup=buyJam2)
    await call.answer()

@database.callback_query_handler(text='buy_jamV1')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@database.callback_query_handler(text='buy_jamV2')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@database.callback_query_handler(text='buy_jamV3')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@database.callback_query_handler(text='buy_jamK')
async def buy_l(call):
    await call.message.answer(text='Выберите объем', reply_markup=buyJam3)
    await call.answer()

@database.callback_query_handler(text='buy_jamK1')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@database.callback_query_handler(text='buy_jamK2')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@database.callback_query_handler(text='buy_jamK3')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@database.callback_query_handler(text='buy_jamE')
async def buy_l(call):
    await call.message.answer(text='Выберите объем', reply_markup=buyJam4)
    await call.answer()

@database.callback_query_handler(text='buy_jamE1')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@database.callback_query_handler(text='buy_jamE2')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@database.callback_query_handler(text='buy_jamE3')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(database, skip_updates=True)