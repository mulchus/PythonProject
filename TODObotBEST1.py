from random import choice
import datetime
import telebot
#������ �� ��������. ������ ���

token = '5430864257:AAHsIGljFlHg_BpYoW7o9AKqi4Q-hw6tNRc'

bot = telebot.TeleBot(token)


RANDOM_TASKS = ['�������� ����� ������', '������� Python', '���������� �� ���� � ���������', '���������� 4 ����� ��� � �����']

todos = dict()
todos_vrem = dict()


HELP = '''
������ ��������� ������:
* print, show  - �������� ��� ������ �� �������� ����
* add - �������� ������ (������ /add ���� ����� ��-��-�� ��-��. �������� ���� ������ ���� '�������' ��� '������'")
* random - �������� �� ������� ��������� ������
* help - ���������� help

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
    bot.send_message(message.chat.id, f'������ {task} ��������� �� {date_now} {time_now}')


@bot.message_handler(commands=['add'])
def add(message):
    _, date, time, tail = message.text.split(maxsplit=3)
    task = ' '.join([tail])
    if '�������' in date.lower():
        date = datetime.datetime.strftime(datetime.datetime.now(), "%d-%m-%y")
    elif '������' in date.lower():
        date = datetime.datetime.strftime(datetime.datetime.now()+datetime.timedelta(days=1), "%d-%m-%y")
    try:
        dateForm = datetime.datetime.strptime(date, "%d-%m-%y")
        timeForm = datetime.datetime.strptime(time, "%H-%M")
    except (TypeError, ValueError, IndexError):
        bot.send_message(message.chat.id, f'���� ��� ����� ������� � �������� �������: {date} {time}. ��������� ��-��-�� ��-��')
    else:
        add_todo(dateForm, timeForm, task)
        bot.send_message(message.chat.id, f'������ {task} ��������� �� ���� {dateForm.strftime("%d-%m-%y")} ����� {timeForm.strftime("%H-%M")}')


@bot.message_handler(commands=['print', 'show'])
def print_(message):
    try:
        dateForm = datetime.datetime.strptime(message.text.split()[1].lower(), "%d-%m-%y")
        #timeForm = datetime.datetime.strptime(message.text.split()[2].lower(), "%H-%M")
    except (TypeError, ValueError):
        bot.send_message(message.chat.id, '���� ������� � �������� �������. ���������: ��-��-��')
    except IndexError: #����� �����, ���� ������ ���� ������� (�� ����� �������� ���� �� ������� 1)
        if not len(todos):
            tasks = '���� �� ����� ������ �� ���������'
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
            tasks = '����� �� ����� ���� � ������� ���'
        bot.send_message(message.chat.id, tasks)

bot.polling(none_stop=True)