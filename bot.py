import telebot

TOKEN = 'There is your telegram bot token'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    
    if message.from_user.id != bot.get_me().id:
        bot.reply_to(message, "Я ебал внеурочку")

bot.polling()
