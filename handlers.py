from telebot import types
import os

class BotHandlers:
    def __init__(self, bot, intel):
        self.bot = bot
        self.intel = intel

    def menu_principal(self, message):
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_financas = types.InlineKeyboardButton("💰 Finanças", callback_data="btn_financas")
        btn_jobs = types.InlineKeyboardButton("🚀 Jobs/PJ", callback_data="btn_jobs")
        btn_dark = types.InlineKeyboardButton("📺 Canal Dark", callback_data="btn_dark")
        
        markup.add(btn_financas, btn_jobs, btn_dark)
        self.bot.send_message(message.chat.id, "🛠️ **Painel ROBLab**\nEscolha o braço de execução:", reply_markup=markup, parse_mode="Markdown")

    def analisar_financas(self, message):
        if os.path.exists("noticias.json"):
            with open("noticias.json", "r", encoding="utf-8") as f:
                dados = f.read()
            prompt = f"Analise como ROBLab: {dados}. Sugira 3 ações para quitar a sogra e juntar 35k."
            res = self.intel.ask(prompt)
            self.bot.send_message(message.chat.id, res)
        else:
            self.bot.send_message(message.chat.id, "⚠️ notícias.json não encontrado.")

    def analisar_jobs(self, message):
        if os.path.exists("jobs.json"):
            with open("jobs.json", "r", encoding="utf-8") as f:
                vagas = f.read()
        
            # Prompt de "Ataque" para ganhar o freela
            prompt = (
                f"Você é o Headhunter do ROBLab. Analise estas vagas: {vagas}. "
                "1. Identifique as 2 melhores para um desenvolvedor Python/PJ. "
                "2. Para cada uma, escreva uma proposta curta e matadora (em inglês e português) "
                "focada em entrega rápida e qualidade técnica. "
                "Seja direto, sem enrolação."
            )
        
            res = self.intel.ask(prompt)
            self.bot.send_message(message.chat.id, res)
        else:
            self.bot.send_message(message.chat.id, "⚠️ jobs.json não encontrado. Rode o minerador primeiro!")