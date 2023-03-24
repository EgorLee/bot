import telebot
import schedule
import time
from requests_html import HTMLSession


COOKIES = {
    'PHPSESSID': '72638anahgdol5ljtnfdnv6bt3',
    '_csrf': '2fedb06d384279eb35bc1809eaec1a9c07baba9f0e6614fbf7b5b2c3895d4038a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22'
             '_csrf%22%3Bi%3A1%3Bs%3A32%3A%222PjRKwWO3Ko4w5EnG6NvqgqV2_cdVyhN%22%3B%7D',
    'destrict': '1936',
    'geoplace': '049bc2fea23868dd45e45d54aee47154dc773e4fd3d607a6a7161ce8c7ce4509a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%'
                '22geoplace%22%3Bi%3A1%3Bs%3A228%3A%22eyJsYXQiOjU5LjQzMywibG5nIjoyNC43MzIzLCJjaXR5IjoiXHUwNDIyXHU'
                'wNDMwXHUwNDNiXHUwNDNiXHUwNDM4XHUwNDNkIiwiY291bnRyeSI6Ilx1MDQyZFx1MDQ0MVx1MDQ0Mlx1MDQzZVx1MDQzZFx1'
                'MDQzOFx1MDQ0ZiIsImlwIjoiMTg1LjMxLjk0LjU0IiwiYXJlYSI6IiIsInJlZ2lvbiI6IiJ9%22%3B%7D',
    'isMinskIp': 'false',
    'region-delivery': '94',
    'regionId': '1',
}

HEADERS = {
    #'Content-Type': 'application/json; boundary=----WebKitFormBoundaryRXpwPvAdaVI1zm6T',
    'Cookie': 'PHPSESSID=72638anahgdol5ljtnfdnv6bt3; _csrf=2fedb06d384279eb35bc1809eaec1a9c0'
              '7baba9f0e6614fbf7b5b2c3895d4038a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%222Pj'
              'RKwWO3Ko4w5EnG6NvqgqV2_cdVyhN%22%3B%7D; destrict=1936; geoplace=049bc2fea23868dd45e45d54aee47154dc'
              '773e4fd3d607a6a7161ce8c7ce4509a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22geoplace%22%3Bi%3A1%3Bs%3A228%3A%22eyJsYX'
              'QiOjU5LjQzMywibG5nIjoyNC43MzIzLCJjaXR5IjoiXHUwNDIyXHUwNDMwXHUwNDNiXHUwNDNiXHUwNDM4XHUwNDNkIiwiY291bnRy'
              'eSI6Ilx1MDQyZFx1MDQ0MVx1MDQ0Mlx1MDQzZVx1MDQzZFx1MDQzOFx1MDQ0ZiIsImlwIjoiMTg1LjMxLjk0LjU0IiwiYXJlYSI6IiI'
              'sInJlZ2lvbiI6IiJ9%22%3B%7D; isMinskIp=false; region-delivery=94; regionId=1',
}

DATA = {
    #'Content-Type': 'application/json',
    'priceCalculate-contactRadio': 'Phone',
    'name': 'BOT TEST',
    'tel': '+7 (111) 111-11-11',
    'region-delivery': '94',
    "url": "https://www.lbr.ru/traktory/mtz/82-1",
    "model_name": "82.1",
    "type": "tech"
}


def get_form(url):
    with HTMLSession() as session:
        resp = session.post(url, data=DATA, headers=HEADERS, cookies=COOKIES)
        return resp


def send_message(text):
    chat_id = 1047113787
    bot = telebot.TeleBot('6000652427:AAFjoz8uuhplWRlg5vJu2Wh8NI1e5BKD-68')
    bot.send_message(chat_id, text)


def run():
    url = 'https://www.lbr.ru/widget-handler/get-price-form'
    response = get_form(url)

    try:
        data = response.json()
    except Exception:
        data = "Not Found"
    print(f"{response.status_code} : {data}")

    if response.status_code == 200 and data == 1:
        message_text = f"Форма работает. Код ответа : {response.status_code}"
    if response.status_code == 400:
        message_text = f"Проблема с отправкой формы. Код ответа : {response.status_code}"
    if not response.status_code == 400 and not response.status_code == 200:
        message_text = f"Форма не работает. Код ответа : {response.status_code}"
    send_message(message_text)


if __name__ == '__main__':
    schedule.every().day.at("11:11").do(run)
    while True:
        schedule.run_pending()
        time.sleep(1)