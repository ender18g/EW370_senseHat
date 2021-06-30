import argparse
from sense_hat import SenseHat, ACTION_RELEASED
from random import randint
from display_text import show_text
import time
import requests

sense = SenseHat()
sense.clear()


def red(event):
    if event.action != ACTION_RELEASED:
        sense.clear(255, 0, 0)
        print('red')


def showtime(event):
    if event.action != ACTION_RELEASED:
        mil_time = time.strftime("%H%M", time.localtime())
        print(mil_time)
        show_text(mil_time)


def show_btc(event):
    if event.action != ACTION_RELEASED:
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        response = requests.get(url)
        btc_dict = response.json()
        btc_price = btc_dict.get('bpi').get('USD').get('rate')
        btc_price = btc_price.split('.')[0]
        btc_price = '$' + btc_price
        print(btc_price)
        show_text(btc_price)


sense.stick.direction_up = red
sense.stick.direction_down = showtime
sense.stick.direction_right = show_btc

while True:
    pass
