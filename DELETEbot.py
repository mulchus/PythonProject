import telebot
from datetime import datetime
from datetime import time

token = '5430864257:AAHsIGljFlHg_BpYoW7o9AKqi4Q-hw6tNRc'
bot = telebot.TeleBot(token)

user = ''
time_start = ''
time_end = ''


# @bot.message_handler(content_types=['text'])
# def echo(message):
#     #print(message)
#     pass

@bot.message_handler(commands=['start'])
def start(message):
    GROUP_ID = message.chat.id
    bot.send_message(message.chat.id, f'GROUP_ID = {message.chat.id}')
    return GROUP_ID


@bot.message_handler(commands=['delete']) #, func=lambda message: message.entities is not None and message.chat.id == message.chat.id )
def delete(message):
    #print(message)
    _, user, time_1, time_2 = message.text.split(maxsplit=3)
    print(datetime.fromtimestamp(message.date+10800).strftime("%H:%M"))

    time_start = datetime.combine(datetime.now().date(), datetime.strptime(time_1, "%H-%M").time())
    time_start_sec = int((time_start-datetime(1970,1,1)).total_seconds()-10800)
    print(time_start)
    print(time_start_sec)
    time_end = datetime.combine(datetime.now().date(), datetime.strptime(time_2, "%H-%M").time())
    time_end_sec = int((time_end-datetime(1970,1,1)).total_seconds()-10800)
    print(time_end)
    print(time_end_sec)

    print(message.from_user.username, message.chat.id, message.id)
    #for i in range(time_end_sec, time_start_sec, -1):

    #��� ����� ���� ��������� ��������� �� ������ ���������� ���������
    for entity in message.entities:  # �������� �� ���� entities � ������� ������

        # url - ������� ������, text_link - ������, ������� ��� �������

        if message.from_user.username == user and message.date in range(time_start_sec, time_end_sec):
            print(message.date)
            # �� ����� �� ��������� chat.id, �� ����������� ��� � ��������
            bot.delete_message(message.chat.id, message.message_id)
        else:
            return

# @bot.message_handler(func=lambda message: message.entities is not None and message.chat.id == message.chat.id)
# def delete_links(message):
#     for entity in message.entities:  # �������� �� ���� entities � ������� ������
#         # url - ������� ������, text_link - ������, ������� ��� �������
#         if entity.type in ["url", "text_link"]:
#             # �� ����� �� ��������� chat.id, �� ����������� ��� � ��������
#             bot.delete_message(message.chat.id, message.message_id)
#         else:
#             return

    #time_start = datetime.fromtimestamp(time_1).strftime("%H:%M")
    #time_end = datetime.fromtimestamp(time_2).strftime("%H:%M")



    # print(msg)
    # time.sleep(2)
    # bot.edit_message_text(chat_id = message.chat.id, message_id = msg.message_id, text = f'��, �� ������� "{message.text}"')
    # tb.edit_message_text(new_text, chat_id, message_id)
    # photo = open('/tmp/photo.png', 'rb')
    # tb.send_photo(chat_id, photo)
    # tb.send_photo(chat_id, "FILEID")

bot.polling(none_stop=True)