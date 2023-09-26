#!/venv/bin python
# -*- coding: utf-8 -*-
#project: AvgustAmbulance

import subprocess
from subprocess import Popen, PIPE
import sys, os
import telebot #pip install pyTelegramBotAPI
from telebot import types
import configparser

#Читаем файл конфигов
config = configparser.RawConfigParser()
config.read("./global_config.conf")

#Вытаскиваем из конфигов списки
userList = config.get("lists", "userList").split(',')
adminList = config.get("lists", "adminList").split(',')

#Преобразуем элементы списков из str в int
userList = [int(i) for i in userList]
adminList = [int(i) for i in adminList]

#Считываем пути из конфигов
script_neuron = config.get("path", "script_neuron")
photoPath = config.get("path", "photo_dir")

treeFlag = 0

#В TOKEN должен находиться ваш токен, полученый при создании бота!
#замените значение на свои данные!

TOKEN = "...."

bot = telebot.TeleBot(TOKEN)


# Клавиатура узнать айдишник
markupid = telebot.types.ReplyKeyboardMarkup(True)
markupid.row('Узнать свой ID')

# Админский старт)
markupadmin = telebot.types.ReplyKeyboardMarkup(True)
markupadmin.row('Сканирование')
markupadmin.row('Подбор препаратов')
markupadmin.row('Информация')
markupadmin.row('Добавить ID нового пользователя')


#Клавиатура №1
markup = telebot.types.ReplyKeyboardMarkup(True)
markup.row('Сканирование')
markup.row('Подбор препаратов')
markup.row('Информация')
#itembtn4 = types.KeyboardButton('Прислать свой номер', request_contact=True)
#itembtn5 = types.KeyboardButton('Прислать свою локацию', request_location=True)


#Клавиатура №2
markup2 = telebot.types.ReplyKeyboardMarkup(True)
markup2.row('Яблоня', 'Вишня')
markup2.row('Главное меню')

#Клавиатура №3
markup3 = telebot.types.ReplyKeyboardMarkup(True)
markup3.row('Лист', 'Ветка', 'Дерево')
markup3.row('Главное меню')


#Клавиатура №4
markup4 = types.ForceReply(selective=False)


#Клавиатура №5
markup5 = types.InlineKeyboardMarkup()
url_button = types.InlineKeyboardButton(text="Перейти на avgust.com", url="https://avgust.com")
markup5.add(url_button)


#Клавиатура №6 Раёк
markup6 = types.InlineKeyboardMarkup()
url_button = types.InlineKeyboardButton(text="Раёк® :)", url="http://dacha.avgust.com/catalog/rayek/")
markup6.add(url_button)


#Клавиатура №7
markup7 = telebot.types.ReplyKeyboardMarkup(True)
markup7.row('Загрузить еще фото')
markup7.row('Подобрать препарат')
markup7.row('Главное меню')


#Для определения айдишника стикеров:)
@bot.message_handler(content_types=['sticker'])
def start_message(message):
    print(message)


@bot.message_handler(commands=['start'])
def start_message(message):
    # print(message) #Для отладки - просмотр всех параметров сообщения
    if (message.from_user.id in adminList) and (message.from_user.id in userList):
        bot.send_message(message.from_user.id, 'Ты че админ шоле?', reply_markup=markupadmin)
        bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAANlXzbd_FdycU15vvPiwTIGsDbLjHwAAgYBAAJTKD4K2t0JmfwdmjMaBA')
    elif message.from_user.id in userList:
        print('Chat:', message.content_type)
        print("id отправителя сообщения: " + str(message.from_user.id))
        print("id группы: " + str(message.chat.id))
        print(message.text)
        treeFlag = 0
        bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAIIh18G0eRWw893Ixj7zJlTzWTGc6ucAAIJAAPANk8T780bokr_cZUaBA')
        bot.send_message(message.from_user.id, 'Здравствуйте! Чем я могу Вам помочь? \U0001F331 \U0001F331 \U0001F331',
                         reply_markup=markup)
    else:
        print("id отправителя сообщения: " + str(message.from_user.id))
        bot.send_message(message.from_user.id,
                         'Вы не имеете доступа к этому боту! Обратитесь к разработчикам за разрешением!',
                         reply_markup=markupid)

@bot.message_handler(commands=['url'])
def default_test(message):
    if message.from_user.id in userList:
        print('Chat:', message.content_type)
        print("id отправителя сообщения: " + str(message.from_user.id))
        print("id группы: " + str(message.chat.id))
        print(message.text)
        bot.send_message(message.from_user.id, "Привет! Нажми на кнопку и перейди на сайт.", reply_markup=markup5)
    else:
        bot.send_message(message.from_user.id, 'Вы не имеете доступа к этому боту! Обратитесь к разработчикам за разрешением.')

@bot.message_handler(content_types=['text'])
def send_text(message):
    global treeFlag
    global userList
    if message.from_user.id in userList:
        print('Chat:', message.content_type)
        print("id отправителя сообщения: " + str(message.from_user.id))
        print("id группы: " + str(message.chat.id))
        print(message.text)

        if message.text.lower() == 'главное меню':
            treeFlag = 0
            bot.send_message(message.from_user.id, 'Выберите раздел', reply_markup=markup)
        elif message.text.lower() == 'сканирование':
            bot.send_message(message.from_user.id, 'Выберите объект сканирования:', reply_markup=markup2)
        elif message.text.lower() == 'подбор препаратов':
            bot.send_message(message.from_user.id, 'Раздел в разработке')
            bot.send_sticker(message.from_user.id,
                             'CAACAgIAAxkBAAIIqV8G1G8TLk2KjS682Hs2kI87-5NFAALqAANTKD4K1OTuxuzd7pMaBA')
        elif message.text.lower() == 'информация':
            bot.send_message(message.from_user.id, 'Для более подробной информации посетите наш сайт!',
                             reply_markup=markup5)
        elif message.text.lower() == 'яблоня':
            bot.send_message(message.from_user.id, 'Какую часть растения вы хотите мне прислать?', reply_markup=markup3)
            treeFlag = 1
        elif message.text.lower() == 'вишня':
            bot.send_message(message.from_user.id, 'Какую часть растения вы хотите мне прислать?', reply_markup=markup3)
            treeFlag = 1
        elif message.text.lower() == 'лист':
            bot.send_message(message.from_user.id, 'Приложите фотографию', reply_markup=markup4)
            treeFlag = 1
        elif message.text.lower() == 'ветка':
            bot.send_message(message.from_user.id, 'Приложите фотографию', reply_markup=markup4)
            treeFlag = 1
        elif message.text.lower() == 'дерево':
            bot.send_message(message.from_user.id, 'Приложите фотографию', reply_markup=markup4)
            treeFlag = 1
        elif message.text.lower() == 'загрузить еще фото':
            bot.send_message(message.from_user.id, 'Приложите фотографию', reply_markup=markup4)
            treeFlag = 1
        elif message.text.lower() == 'подобрать препарат' and treeFlag == 2:
            bot.send_message(message.from_user.id, 'Вам поможет наш Высокоэффективный препарат для обработки плодовых культур от болезней - Раёк, КЭ', reply_markup=markup6)
            treeFlag = 0
        elif message.text.lower() == 'добавить id нового пользователя':
            bot.send_message(message.from_user.id, 'Ну добавляй')
            treeFlag = 'id'
        elif treeFlag == 'id':
            newid = message.text.lower()
            userList.append(int(newid))
            treeFlag = 0
            bot.send_message(message.from_user.id, 'Добавил!', reply_markup=markupadmin)
            newidList = userList
            change_userList(newidList)
        else:
            bot.send_message(message.from_user.id, 'Я не понимаю тебя...', reply_markup=markup)
            treeFlag = 0
    else:
        if message.text.lower() == 'узнать свой id':
            bot.send_message(message.from_user.id, message.from_user.id)
            bot.send_message(message.from_user.id, 'Сообщите Ваш id администратору бота и обновите историю сообщений')
        else:
            print("id отправителя сообщения: " + str(message.from_user.id))
            bot.send_message(message.from_user.id,
                             'Вы не имеете доступа к этому боту! Обратитесь к разработчикам за разрешением.')


@bot.callback_query_handler(func=lambda call: True)
def on_callback(call):
    #print(call) #Для отладки
    if call.from_user.id in userList:
        print('Callback query:', call.message.content_type, call.data)
        print("id отправителя сообщения: " + str(call.from_user.id))
        print("id группы: " + str(call.message.chat.id))

        bot.answer_callback_query(callback_query_id=call.id, text='Пришлите фото', show_alert=True)
    else:
        bot.send_message(call.from_user.id, 'Вы не имеете доступа к этому боту! Обратитесь к разработчикам за разрешением.')

#Скрипт открывает скрипт и фотку
def script_open(photo_name):
    out, err = Popen(script_neuron + ' ' + str(photo_name), shell=True, stdout=PIPE).communicate()
    out_bot = (str(out, 'utf-8'))
    return(out_bot)

#Функция добавляет айдишник
def change_userList(x):
    # Меняем значения из конфиг. файла.
    config.set("lists", "userList", str(x)[1:-1])
    # Вносим изменения в конфиг. файл.
    with open("./global_config.conf", "w") as config_file:
        config.write(config_file)


#Болд
def test_send_message_with_markdown(self, CHAT_ID=None):
    tb = telebot.TeleBot(TOKEN)
    markdown = """
    *bold text*
    _italic text_
    [text](URL)
    """
    ret_msg = tb.send_message(CHAT_ID, markdown, parse_mode="Markdown")
    assert ret_msg.message_id

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    global treeFlag
    if message.from_user.id in userList:
        print('Chat:', message.content_type)
        print("id отправителя сообщения: " + str(message.from_user.id))
        print("id группы: " + str(message.chat.id))
#        print(message.photo)

        if treeFlag == 0:
            bot.send_message(message.chat.id, 'Вы не выбрали объект сканирования. Определитесь с культурой и отправьте фото еще раз', reply_markup=markup2)
        else:
            try:
                file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
#                print(file_info) - айдишник фотки с джипегом
                filename, file_extension = os.path.splitext(file_info.file_path)
                downloaded_file = bot.download_file(file_info.file_path)
                src = photoPath + message.photo[1].file_id + file_extension
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)
                bot.reply_to(message, "Фото получено и обрабатывается! Это займет несколько секунд...")
                x = script_open(message.photo[1].file_id)
                print(x)
                if x.find('patology is scab') != -1:
                    if x.find('1.00') != -1:
                        bot.send_message(message.from_user.id, 'Хм...на 100% уверен, что это [парша](https://www.avgust.com/atlas/b/detail.php?ID=2010)', parse_mode='Markdown')
                        bot.send_message(message.from_user.id, ':(', reply_markup=markup7)
                    else:
                        bot.send_message(message.from_user.id, 'Хм...на ' + x[2:4] + '% уверен, что это [парша](https://www.avgust.com/atlas/b/detail.php?ID=2010)', parse_mode='Markdown')
                        bot.send_message(message.from_user.id, ':(', reply_markup=markup7)
                    treeFlag = 2
                elif x.find('patology is healthy') != -1:
                    bot.send_message(message.from_user.id, 'У меня хорошие новости - ваше растение здорово!!! :)')
                    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAIP418WCmadBQyCXpTMTTYRL_yhVSS7AAKFywACY4tGDCX6oFTalYa_GgQ', reply_markup=markup7)
                elif x.find('patology is rust') != -1:
                    if x.find('1.00') != -1:
                        bot.send_message(message.from_user.id, 'Хм...на 100% уверен, что это [ржавчина](http://dacha.avgust.com/for-garden-home/directory-page/rzhavchina/)', parse_mode='Markdown')
                        bot.send_message(message.from_user.id, ':(', reply_markup=markup7)
                    else:
                        bot.send_message(message.from_user.id, 'Хм...на ' + x[7:9] + '% уверен, что это [ржавчина](http://dacha.avgust.com/for-garden-home/directory-page/rzhavchina/)', parse_mode='Markdown')
                        bot.send_message(message.from_user.id, ':(', reply_markup=markup7)
                    treeFlag = 2
                elif x.find('patology is klyasterosporioz') != -1:
                    if x.find('1.00') != -1:
                        bot.reply_to(message, 'Хм...на 100% уверен, что это [клястероспориоз](http://www.pesticidy.ru/%D0%9A%D0%BB%D1%8F%D1%81%D1%82%D0%B5%D1%80%D0%BE%D1%81%D0%BF%D0%BE%D1%80%D0%B8%D0%BE%D0%B7)', parse_mode='Markdown')
                        bot.send_message(message.from_user.id, ':(', reply_markup=markup7)
                    else:
                        bot.reply_to(message, 'Хм...на ' + x[17:19] + '% уверен, что это [клястероспориоз](http://www.pesticidy.ru/%D0%9A%D0%BB%D1%8F%D1%81%D1%82%D0%B5%D1%80%D0%BE%D1%81%D0%BF%D0%BE%D1%80%D0%B8%D0%BE%D0%B7)', parse_mode='Markdown')
                        bot.send_message(message.from_user.id, ':(', reply_markup=markup7)
                    treeFlag = 2
                elif x.find('patology is cocomyces') != -1:
                    if x.find('1.00') != -1:
                        bot.send_message(message.from_user.id, 'Хм...на 100% уверен, что это [коккомикоз](http://www.pesticidy.ru/%D0%9A%D0%BE%D0%BA%D0%BA%D0%BE%D0%BC%D0%B8%D0%BA%D0%BE%D0%B7)', parse_mode='Markdown')
                        bot.send_message(message.from_user.id, ':(', reply_markup=markup7)
                    else:
                        bot.send_message(message.from_user.id, 'Хм...на ' + x[12:14] + '% уверен, что это [коккомикоз](http://www.pesticidy.ru/%D0%9A%D0%BE%D0%BA%D0%BA%D0%BE%D0%BC%D0%B8%D0%BA%D0%BE%D0%B7)', parse_mode='Markdown')
                        bot.send_message(message.from_user.id, ':(', reply_markup=markup7)
                    treeFlag = 2
                elif x.find('patology is multipleDiseases') != -1:
                    bot.send_message(message.from_user.id, 'Ой-оооой, похоже, что ваше растение поражено несколькими заболеваниями...', reply_markup=markup7)


#Айдишник фотографии
#                print(message.photo[1].file_id)

            except Exception as e:
                bot.reply_to(message,e )

#            bot.send_message(message.from_user.id, 'Изучаю, минутку', reply_markup=markup)
#            treeFlag=0
    else:
        bot.send_message(message.from_user.id, 'Вы не имеете доступа к этому боту! Обратитесь к разработчикам за разрешением.')

print('Listening ...')
bot.polling()
