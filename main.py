from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import time
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(f'Welcome, {update.effective_user.first_name}! Цей бот засікає час для збільшення вашої продуктивності 😝😁🙃')


def help(update: Update, context: CallbackContext):
    update.message.reply_text(f'/select_program  Викличіть цю команду щоб вибрити програму\n'
                              f'/start_timer Викличіть цю команду щоб почати секундомір\n'
                              f'/stop_timer Викличіть цю команду щоб зупинити секундомір\n'
                              f'/check_info Викличіть цю команду щоб побачити вашу інформацію\n'
                              f'/clear_data Викличіть цю команду щоб очистити вашу інформацію\n'
                              f'/start_pause Викличіть цю команду щоб почати паузу\n'
                              f'/stop_pause Викличіть цю команду щоб закінчити паузу')


def select_program(update: Update, context: CallbackContext):
    select_program.has_been_called = True
    update.message.reply_text('Програми вибрана')
    program = ''.join(context.args)
    try:
        with open('data.txt', 'r') as data:
            old_program = data.read()
    except FileNotFoundError:
        old_program = ''
    with open('data.txt', 'w') as data:
        data.write(f'{old_program}\n{program}')

select_program.has_been_called = False

def start_timer(update: Update, context: CallbackContext):
    if select_program.has_been_called:
        start_timer.has_been_called = True
        global start_time
        start_time = time.time()
        update.message.reply_text('Секундомір запушено')
        times = ''.join(context.args)
        try:
            with open('times.txt', 'r') as timet:
                old_times = timet.read()
        except FileNotFoundError:
            old_times = ''
        with open('times.txt', 'w') as timet:
            timet.write(f'{old_times}\n{times}')
    else:
        update.message.reply_text('Спочатку виберіть програму')

start_timer.has_been_called = False

def stop_timer(update: Update, context: CallbackContext):
    if start_timer.has_been_called == True:
        stop_timer.has_been_called = True
        update.message.reply_text('Секундомір закінчино')
        end_time = time.time()
        timerr = end_time - start_time
        timerr = str(timerr)
        with open('times.txt', 'r') as data:
            old_time = data.read()
        with open('times.txt', 'w') as times:
            times.write(f'{old_time}\n{timerr}')
    else:
        update.message.reply_text("Спочатку запустіть секундомір")
    start_timer.has_been_called = False

stop_timer.has_been_called = False

def start_pause(update: Update, context: CallbackContext):
    if start_timer.has_been_called:
        start_pause.has_been_called = True
        update.message.reply_text('Паузу почато')
        global start_paisa_time
        start_paisa_time = time.time()
        paisa_times = ''.join(context.args)
        try:
            with open('paisa.txt', 'r') as paisa_time:
                old_paisa_time = paisa_time.read()
        except FileNotFoundError:
            old_paisa_time = ''
        with open('paisa.txt', 'w') as timet:
            timet.write(f'{old_paisa_time}\n{paisa_times}')
    else:
        update.message.reply_text('Спочатку запустіть секундомір')

start_pause.has_been_called = False

def stop_pause(update: Update, context: CallbackContext):
    if start_pause.has_been_called:
        update.message.reply_text('Паузу закінчено')
        stop_paisa_time = time.time()
        paisa_timer = stop_paisa_time - start_paisa_time
        paisa_timer = str(paisa_timer)
        with open('paisa.txt', 'r') as paisa:
            old_paisa = paisa.read()
        with open('paisa.txt', 'w') as paisa:
            paisa.write(f'{old_paisa}\n{paisa_timer}')
    else:
        update.message.reply_text('Спочатку почніть паузу')
    start_pause.has_been_called = False


def check_info(update: Update, context: CallbackContext):
    with open('data.txt') as data:
        for lines in data:
            pass
        info = lines
    with open('times.txt') as datas:
        for line in datas:
            pass
    with open('paisa.txt') as paisa:
        for last_line in paisa:
            pass
    last_pause = last_line
    last_pause = round(float(last_pause))
    last_time = line
    last_time = round(float(last_time))
    update.message.reply_text(f'Ваша програма - {info}❤. \nВаш час {(last_time - last_pause) / 60} хв. \nВаша пауза{last_pause / 60} хв.')


def clear_data(update: Update, context: CallbackContext):
    clear = open('data.txt', 'r+')
    clear.truncate(0)
    clears = open('times.txt', 'r+')
    clears.truncate(0)
    clears = open('paisa.txt', 'r+')
    clears.truncate(0)
    update.message.reply_text('Вашу інформацію очишчено')



def main():
    updater = Updater('5777598816:AAHnfFqLwXT-QIG5csvf-yQ1sTC7lJTh-Wk')
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('select_program', select_program))
    dispatcher.add_handler(CommandHandler('start_timer', start_timer))
    dispatcher.add_handler(CommandHandler('start_pause', start_pause))
    dispatcher.add_handler(CommandHandler('clear_data', clear_data))
    dispatcher.add_handler(CommandHandler('check_info', check_info))
    dispatcher.add_handler(CommandHandler('stop_timer', stop_timer))
    dispatcher.add_handler(CommandHandler('stop_pause', stop_pause))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


