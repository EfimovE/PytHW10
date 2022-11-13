from aiogram import Dispatcher
import commands

def registred_handlers (dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])
    # dp.register_message_handler(commands.help, commands=['help'])
    dp.register_message_handler(commands.set_count, commands=['set_count'])
    dp.register_message_handler(commands.playerTurn)
    