from random import choice
import datetime
import telebot
#ничего не менялось. просто пуш

token = '5430864257:AAHsIGljFlHg_BpYoW7o9AKqi4Q-hw6tNRc'

bot = telebot.TeleBot(token)


RANDOM_TASKS = ['Написать Гвидо письмо', 'Выучить Python', 'Записаться на курс в Нетологию', 'Посмотреть 4 сезон Рик и Морти']

todos = dict()
todos_vrem = dict()


HELP = '''
Список доступных команд:
* print, show  - напечать все задачи на заданную дату
* add - добавить задачу (формат /add Дата Время ДД-ММ-ГГ ЧЧ-ММ. Возможен ввод вместо даты 'сегодня' или 'завтра'")
* random - добавить на сегодня случайную задачу
* help - Напечатать help

'''


def add_todo(dateForm, timeForm, task):
    if todos.get(dateForm) is not None:
        todos[dateForm].append([timeForm, task])
        todos[dateForm].sort()

    else:
        todos[dateForm] = []
        todos[dateForm].append([timeForm, task])
    print(todos)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['random'])
def random(message):
    task = choice(RANDOM_TASKS)
    date_now = datetime.date.now("%d-%m-%y")
    time_now = datetime.time.now("%H-%M")
    add_todo(date_now, time_now, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на {date_now} {time_now}')


@bot.message_handler(commands=['add'])
def add(message):
    _, date, time, tail = message.text.split(maxsplit=3)
    task = ' '.join([tail])
    if 'сегодня' in date.lower():
        date = datetime.datetime.strftime(datetime.datetime.now(), "%d-%m-%y")
    elif 'завтра' in date.lower():
        date = datetime.datetime.strftime(datetime.datetime.now()+datetime.timedelta(days=1), "%d-%m-%y")
    try:
        dateForm = datetime.datetime.strptime(date, "%d-%m-%y")
        timeForm = datetime.datetime.strptime(time, "%H-%M")
    except (TypeError, ValueError, IndexError):
        bot.send_message(message.chat.id, f'Дата или время введено в неверном формате: {date} {time}. Правильно ДД-ММ-ГГ ММ-ЧЧ')
    else:
        add_todo(dateForm, timeForm, task)
        bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {dateForm.strftime("%d-%m-%y")} время {timeForm.strftime("%H-%M")}')


@bot.message_handler(commands=['print', 'show'])
def print_(message):
    try:
        dateForm = datetime.datetime.strptime(message.text.split()[1].lower(), "%d-%m-%y")
        #timeForm = datetime.datetime.strptime(message.text.split()[2].lower(), "%H-%M")
    except (TypeError, ValueError):
        bot.send_message(message.chat.id, 'Дата введена в неверном формате. Правильно: ДД-ММ-ГГ')
    except IndexError: #вывод всего, если вместо даты пустота (не будет значения даты по индексу 1)
        if not len(todos):
            tasks = 'Пока ни одной задачи не добавлено'
        else:
            tasks = ''
            for i in todos.keys():
                for timetask in todos[i]:
                    tasks += f'{datetime.datetime.strftime(i, "%d-%m-%y")} {datetime.datetime.strftime(timetask[0], "%H-%M")} {timetask[1]}\n'
        bot.send_message(message.chat.id, tasks)
    else:
        if dateForm in todos:
            tasks = ''
            for timetask in todos[dateForm]:
                tasks += f'{datetime.datetime.strftime(dateForm, "%d-%m-%y")} {datetime.datetime.strftime(timetask[0], "%H-%M")} {timetask[1]}\n'
        else:
            tasks = 'Задач на такую дату в записях нет'
        bot.send_message(message.chat.id, tasks)

bot.polling(none_stop=True)