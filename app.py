import telebot
from brain import Intelligence
from handlers import BotHandlers
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)
intel = Intelligence()
interface = BotHandlers(bot, intel)

@bot.message_handler(commands=['start', 'menu'])
def start(message):
    interface.menu_principal(message)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "btn_financas":
        interface.analisar_financas(call.message)
    elif call.data == "btn_jobs":
        #bot.answer_callback_query(call.id, "Em breve: Minerador de Jobs PJ")
        interface.analisar_jobs(call.message)
    elif call.data == "btn_dark":
        bot.answer_callback_query(call.id, "Em breve: Automação Canal Dark")

@bot.message_handler(func=lambda m: True)
def handle_text(message):
    # Lógica genérica de chat
    res = intel.ask(message.text)
    bot.reply_to(message, res)

if __name__ == "__main__":
    print("🚀 Sistema ROBLab em modo modular iniciado...")
    bot.polling()