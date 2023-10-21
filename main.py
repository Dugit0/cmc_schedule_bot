from datetime import timezone
import datetime
import config
import telebot
import sys
import os
import logging




schedules_path = "schedules"
# get filenames of schedules and cut ".txt"
allouds_mods = list(map(lambda name: name[:-4], os.listdir(schedules_path)))
# set default mod
mods_for_chats = dict()


def open_schedule():
    """
    Returns
    -------
    schedule : dict in format <string> : <list of strings>
        dict in format
            key - mod
            value - list of schedules for each day
    """
    global schedules_path, allouds_mods
    schedule = dict()
    for mod in allouds_mods:
        with open(os.path.join(schedules_path, mod + ".txt"), encoding="utf-8") \
                as schedule_file:
            lines = schedule_file.readlines()
        schedule[mod] = [""] * 7
        count = -1
        for i in range(len(lines)):
            if lines[i] != "#\n":
                schedule[mod][count] += lines[i]
            else:
                count += 1
    return schedule


def get_mod(chat_id):
    global mods_for_chats
    try:
        return mods_for_chats[chat_id]
    except:
        mods_for_chats[chat_id] = allouds_mods[0]
        return allouds_mods[0]


schedule = open_schedule()
with open("names.txt", encoding="utf-8") as names_file:
    names = names_file.read()
bot = telebot.TeleBot(config.token)
logging.basicConfig(level=logging.INFO, filename="log.log", filemode="a", 
                    format="%(asctime)s:%(levelname)s:%(message)s")
logging.info(": Start bot")

@bot.message_handler(commands=["today"])
def command_today(message):
    logging.info(f"CHAT_ID is {message.chat.id}: Call /today")
    cur_date = datetime.datetime.now(timezone.utc) + datetime.timedelta(hours=3)
    day = cur_date.weekday()
    bot.send_message(message.chat.id, schedule[get_mod(message.chat.id)][day], "Markdown")


@bot.message_handler(commands=["tomorrow"])
def command_tomorrow(message):
    logging.info(f"CHAT_ID is {message.chat.id}: Call /tomorrow")
    cur_date = datetime.datetime.now(timezone.utc) + datetime.timedelta(hours=3)
    day = cur_date.weekday()
    bot.send_message(message.chat.id, schedule[get_mod(message.chat.id)][(day + 1) % 7], "Markdown")


@bot.message_handler(commands=["any"])
def command_any(message):
    logging.info(f"CHAT_ID is {message.chat.id}: Call /any")
    markup = telebot.types.InlineKeyboardMarkup()
    buttons = [telebot.types.InlineKeyboardButton(f"{i}", callback_data=f"any_{i}") for i in range(1, 8)]
    markup.row(*buttons)
    bot.send_message(message.chat.id, "Day?", reply_markup=markup)


@bot.message_handler(commands=["ours_today"])
def command_ours_today(message):
    logging.info(f"CHAT_ID is {message.chat.id}: Call /ours_today")
    cur_date = datetime.datetime.now(timezone.utc) + datetime.timedelta(hours=3)
    day = cur_date.weekday()
    bot.send_message(message.chat.id, schedule["Phil237"][day], "Markdown")
    bot.send_message(message.chat.id, schedule["CMC321"][day], "Markdown")


@bot.message_handler(commands=["ours_tomorrow"])
def command_ours_tomorrow(message):
    logging.info(f"CHAT_ID is {message.chat.id}: Call /ours_tomorrow")
    cur_date = datetime.datetime.now(timezone.utc) + datetime.timedelta(hours=3)
    day = cur_date.weekday()
    bot.send_message(message.chat.id, schedule["Phil237"][(day + 1) % 7], "Markdown")
    bot.send_message(message.chat.id, schedule["CMC321"][(day + 1) % 7], "Markdown")


@bot.message_handler(commands=["ours_any"])
def command_ours_any(message):
    logging.info(f"CHAT_ID is {message.chat.id}: Call /ours_any")
    markup = telebot.types.InlineKeyboardMarkup()
    buttons = [telebot.types.InlineKeyboardButton(f"{i}", callback_data=f"ours_any_{i}") for i in range(1, 8)]
    markup.row(*buttons)
    bot.send_message(message.chat.id, "Day?", reply_markup=markup)


@bot.message_handler(commands=["week"])
def command_week(message):
    logging.info(f"CHAT_ID is {message.chat.id}: Call /week")
    for day in range(7):
        bot.send_message(message.chat.id, schedule[get_mod(message.chat.id)][day], "Markdown")


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
    global mods_for_chats, schedule
    if call.data[:3] == "any":
        day = int(call.data[4:]) - 1
        bot.send_message(call.message.chat.id, schedule[get_mod(call.message.chat.id)][day], "Markdown")
    elif call.data[:3] == "mod":
        mods_for_chats[call.message.chat.id] = call.data[4:]
        bot.send_message(call.message.chat.id, f"Вы выбрали расписание группы {mods_for_chats[call.message.chat.id]}")
        logging.info(f"CHAT_ID is {call.message.chat.id}: Mod changed to {mods_for_chats[call.message.chat.id]}")
    elif call.data[:8] == "ours_any":
        day = int(call.data[9:]) - 1
        bot.send_message(call.message.chat.id, schedule["Phil237"][day], "Markdown")
        bot.send_message(call.message.chat.id, schedule["CMC321"][day], "Markdown")


@bot.message_handler(commands=["names"])
def command_names(message):
    logging.info(f"CHAT_ID is {message.chat.id}: Call /names")
    bot.send_message(message.chat.id, names, "html")


@bot.message_handler(commands=["week_parity"])
def command_week_parity(message):
    logging.info(f"CHAT_ID is {message.chat.id}: Call /week_parity")
    cur_date = datetime.datetime.now(timezone.utc) + datetime.timedelta(hours=3)
    week = cur_date.isocalendar().week
    if week % 2:
        message_text = "```\nПредмет / ---\n```"
        bot.send_message(message.chat.id, message_text, "Markdown")
    else:
        message_text = "```\n--- / Предмет\n```"
        bot.send_message(message.chat.id, message_text, "Markdown")

bot.infinity_polling()

print(0)
