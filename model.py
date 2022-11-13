import random
from aiogram import types

user_count = 150
total_count = 150
first_turn = None
take = None

def getFirstTurn():
    return first_turn
def setFirstTurn():
    global first_turn
    first_turn = random.randint(0,1)
def getTake():
    global take
    return take
def setTake(new_take: int):
    global take
    take = new_take
def getCount():
    global total_count
    return total_count
def setCount(count: int):
    global total_count
    total_count = count
def getUserCount():
    global user_count
    return user_count
def setUserCount(count: int):
    global user_count
    user_count = count
def checkWin():
    if getCount() <= 0:
        return True

