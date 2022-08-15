import telebot
from telebot import types 

bot = telebot.TeleBot("5430864257:AAHsIGljFlHg_BpYoW7o9AKqi4Q-hw6tNRc")

#print(dir(telebot.types))

CONTENT_TYPES = ["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
                  "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                  "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                  "migrate_from_chat_id", "pinned_message"]

@bot.message_handler(commands=["takenumber"])
def get_phone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1,
                                         resize_keyboard=True)  # подключаем клавиатуру через дополнение types
    button_phone = types.KeyboardButton(text="send_phone", request_contact=True)  # указываем название кнопки
    keyboard.add(button_phone)  # добавляем кнопку
    bot.send_message(message.chat.id, "Вы можете оправить номер нажав на кнопку send_phone", reply_markup=keyboard)

@bot.message_handler(content_types=CONTENT_TYPES)
def confirming(message):
    if message.content_type == "contact":
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Мы получили ваш номер.", reply_markup=keyboard)
    else:
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Номер не был отправлен.", reply_markup=keyboard)

print("Начали")
bot.polling()  # запуск бота