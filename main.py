from datetime import timezone
import datetime
import config
import telebot




with open("schedule.txt", encoding="utf-8") as schedule_file:
    lines = schedule_file.readlines()
schedule = [""] * 7
count = -1
for i in range(len(lines)):
    if lines[i] != "#\n":
        schedule[count] += lines[i]
    else:
        count += 1

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["today"])
def command_today(message):
    cur_date = datetime.datetime.now(timezone.utc) + datetime.timedelta(hours=3)
    day = cur_date.weekday()
    bot.send_message(message.chat.id, schedule[day], "Markdown")


@bot.message_handler(commands=["tomorrow"])
def command_tomorrow(message):
    cur_date = datetime.datetime.now(timezone.utc) + datetime.timedelta(hours=3)
    day = cur_date.weekday()
    bot.send_message(message.chat.id, schedule[(day + 1) % 7], "Markdown")


@bot.message_handler(commands=["any"])
def command_any(message):
    markup = telebot.types.InlineKeyboardMarkup()
    buttons = [telebot.types.InlineKeyboardButton(f"{i}", callback_data=f"{i}") for i in range(1, 8)]
    markup.row(*buttons)
    bot.send_message(message.chat.id, "Day?", reply_markup=markup)


@bot.message_handler(commands=["names"])
def command_names(message):
    bot.send_message(message.chat.id, "TODO")

bot.infinity_polling()

print(0)