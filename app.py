import telebot
from brain import Intelligence
from handlers import BotHandlers

TOKEN = "8595595411:AAEv1B1jCb-Np9-epIUwdIhB9IXITBb4xps"
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
        bot.answer_callback_query(call.id, "Em breve: Minerador de Jobs PJ")
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