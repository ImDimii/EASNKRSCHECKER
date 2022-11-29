import telebot
from snkrs import ea_us, ea1, ea2, ea3, ea4, ea5
cane=0

bot = telebot.TeleBot("PUT UR TOKEN HERE")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Benvenuto nel checker EA di SNKRS IT! \n⚠ Scrivi /help per scoprire i vari comandi!\nScopo solo informativo!\n by Dimitrino#0126")

@bot.message_handler(commands=["help", "aiuto"])
def handle_start_help(message):
	bot.reply_to(message, "I comandi disponibili sono: \n ▪ /ea per visualizzare l'ultimo accesso esclusivo. \n ▪ /ea2 per visualizzare il secondo accesso esclusivo.\n ▪ /ea3 per visualizzare il terzo accesso esclusivo.\n ▪ /ea4 per visualizzare il quarto accesso esclusivo.\n ▪ /check per controllare lo stato del bot" )

@bot.message_handler(commands=["ea", "esclusivo","e","1"])
def handle_start_help(message):
	bot.reply_to(message, ea1())

@bot.message_handler(commands=["ea2", "esclusivo2","e2", "2"])
def handle_start_help(message):
	bot.reply_to(message, ea2())

@bot.message_handler(commands=["ea3", "esclusivo3","e3","3"])
def handle_start_help(message):
	bot.reply_to(message, ea3())

@bot.message_handler(commands=["ea4", "esclusivo4", "e4", "4"])
def handle_start_help(message):
	bot.reply_to(message, ea4())

@bot.message_handler(commands=["ea5", "esclusivo5", "e5","5"])
def handle_start_help(message):
	bot.reply_to(message, ea5())

@bot.message_handler(commands=["status", "sta", "st", "s"])
def handle_start_help(message):
	bot.reply_to(message, "BOT ONLINE!")

@bot.message_handler(commands=["ea_us","us","u","test"])
def handle_start_help(message):
	bot.reply_to(message, ea_us())

bot.infinity_polling()
