import telebot

BOT_TOKEN = "8335793549:AAGnXk13ImRT6S4yWxuJqJIcqTRERwIMLu0"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Bot is working!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, f"You said: {message.text}")

print("🤖 Bot is running...")
bot.infinity_polling()