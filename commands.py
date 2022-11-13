from random import random
# from aiogram.types import InputFile
from aiogram import types
from create_bot import bot
# import messages
import model 


async def start(message: types.Message):
    # print (message)
    model.setCount(int(model.getUserCount()))
    await bot.send_message(message.from_user.id, f'Привет,  {message.from_user.username},\n' 
                                                f'Смысл этой игры: вы с ботом по очереди берете конфеты. Можно за один раз взять от 1 до 28 конфет. Кто возьмет последние конфеты, тот победил')
    model.setFirstTurn()
    first_turn = model.setFirstTurn()
    if first_turn:
        await playerTake(message)
    else:
        await enemyTurn(message)
async def set_count(message: types.Message):
    count = message.text.split()
    if len(count) == 2:
        model.setUserCount(int(count[1]))
    await bot.send_message(message.from_user.id, f'Стартовое количество конфет изменено, на {model.getUserCount()}')

async def playerTake(message: types.Message):
    # print (message)
    await bot.send_message(message.from_user.id, f'{message.from_user.username}, берите конфеты (не больше 28)')
async def playerTurn(message: types.Message):
    take = None
    if message.text.isdigit():
        if int(message.text) < 0 or int(message.text) > 28:
            await bot.send_message(message.from_user.id, f'Вы должны взять не больше 28 конфет !')
        else:
            take = int(message.text)
            model.setTake(int(message.text))
            model.setCount(model.getCount() - take)
            await bot.send_message(message.from_user.id, f'{message.from_user.username} взял {take} конфет, на столе осталось {model.getCount()}')
            if model.checkWin():
                await bot.send_message(message.from_user.id, f'Вы выиграли !')
                return
            await enemyTurn(message)
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.username}, введите число')

async def enemyTurn(message: types.Message):
    count = model.getCount()
    take = count%29 if count%29 != 0 else random.randint(1,28)
    model.setTake(take)
    model.setCount(count - take)
    await bot.send_message(message.from_user.id, f'Бот взял {model.getTake()} конфет, на столе осталось {model.getCount()}')
    if model.checkWin():
        await bot.send_message(message.from_user.id, f'Бот выиграл !')
        return
    await playerTake(message)