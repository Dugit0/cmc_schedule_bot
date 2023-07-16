from datetime import timezone
import datetime
import config
import telebot
import os
import logging




schedules_path = "schedules"
# get filenames of schedules and cut ".txt"
allouds_mods = list(map(lambda name: name[:-4], os.listdir(schedules_path)))
# set default mod
current_bot_mod = allouds_mods[0]


def open_schedule():
    """
    Returns
    -------
    schedule : list of strings
        list of schedules for each day.

    """
    global schedules_path, current_bot_mod
    with open(os.path.join(schedules_path, current_bot_mod + ".txt"), encoding="utf-8") \
            as schedule_file:
        lines = schedule_file.readlines()
    schedule = [""] * 7
    count = -1
    for i in range(len(lines)):
        if lines[i] != "#\n":
            schedule[count] += lines[i]
        else:
            count += 1
    return schedule


schedule = open_schedule()
bot = telebot.TeleBot(config.token)
logging.basicConfig(level=logging.INFO, filename="log.log", filemode="a", 
                    format="%(asctime)s:%(levelname)s:%(message)s")
logging.info(": Start bot")

@bot.message_handler(commands=["today"])
def command_today(message):
    logging.info(f"CHAT_ID is {message.chat.id}: Call /today")
    cur_date = datetime.datetime.now(timezone.utc) + datetime.timedelta(hours=3)
    day = cur_date.weekday()
    bot.send_message(message.chat.id, schedule[day], "Markdown")


@bot.message_handler(commands=["tomorrow"])
def command_tomorrow(message):
    logging.info(f"CHAT_ID is {message.chat.id}: Call /tomorrow")
    cur_date = datetime.datetime.now(timezone.utc) + datetime.timedelta(hours=3)
    day = cur_date.weekday()
    bot.send_message(message.chat.id, schedule[(day + 1) % 7], "Markdown")


@bot.message_handler(commands=["any"])
def command_any(message):
    logging.info(f"CHAT_ID is {message.chat.id}: Call /any")
    markup = telebot.types.InlineKeyboardMarkup()
    buttons = [telebot.types.InlineKeyboardButton(f"{i}", callback_data=f"any_{i}") for i in range(1, 8)]
    markup.row(*buttons)
    bot.send_message(message.chat.id, "Day?", reply_markup=markup)


@bot.message_handler(commands=["week"])
def command_week(message):
    logging.info(f"CHAT_ID is {message.chat.id}: Call /week")
    for day in range(7):
        bot.send_message(message.chat.id, schedule[day], "Markdown")


@bot.message_handler(commands=["changemod"])
def command_changemod(message):
    logging.info(f"CHAT_ID is {message.chat.id}: Call /changemod")
    markup = telebot.types.InlineKeyboardMarkup()
    for mod in allouds_mods:
        button = telebot.types.InlineKeyboardButton(f"{mod}", callback_data=f"mod_{mod}")    
        markup.add(button)
    bot.send_message(message.chat.id, "Mod?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    global current_bot_mod, schedule
    if call.data[:3] == "any":
        day = int(call.data[4:]) - 1
        bot.send_message(call.message.chat.id, schedule[day], "Markdown")
    elif call.data[:3] == "mod":
        current_bot_mod = call.data[4:]
        schedule = open_schedule()
        bot.send_message(call.message.chat.id, f"Вы выбрали расписание группы {current_bot_mod}")
        logging.info(f"CHAT_ID is {call.message.chat.id}: Mod changed to {current_bot_mod}")
        

bot.infinity_polling()

print(0)
