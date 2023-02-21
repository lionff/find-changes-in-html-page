from bs4 import BeautifulSoup
import time
import requests
import telebot

ad = ''
ad2 = ''

while True:

    url = 'URL' # ссылка для парсинга
    token = 'TOKEN' # токен бота
    bot = telebot.TeleBot(token)
    chat_id = 'ID' # айди бота

# делаем запрос и получаем html
    html_text = requests.get(url).text


# используем парсер lxml
    soup = BeautifulSoup(html_text, 'lxml')

    if ad == ad2:
        ad = soup.find('span', class_='b-text b-text_lang_en') # вытаскиваем определенную строку
    if ad != ad2:
        bot.send_message(chat_id, ad) # если появилось изменение - отправка сообщения
        ad2 = ad        
    #print(ad.text)
    #print(ad2.text)
    time.sleep(1200)