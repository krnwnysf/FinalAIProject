# mengimport package pyTelegramBotAPI
import telebot

# inisialisasi Token Bot Kita
bot = telebot.TeleBot('5724299568:AAGvAs5qzrcQKPnfkGBoITaQR5d2Cl9ED6o')

# Menghandle Pesan /start
@bot.message_handler(commands=['start'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Halo, ada apa?')

@bot.message_handler(commands=['help'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Ada yang bisa saya bantu?')

@bot.message_handler(commands=['who?'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Saya adalah bot')

@bot.message_handler(commands=['creator'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Saya dibuat oleh Kurniawan Yusuf')

@bot.message_handler(commands=['how?'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Saya dibuat dengan menggunakan python')


@bot.message_handler(commands=['why?'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Saya dibuat untuk tugas kecerdasan buatan')

@bot.message_handler(commands=['end'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Sampai jumpa :)')

print('bot start running')
bot.polling()