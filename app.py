import telebot
import google.generativeai as genai
import re
import os

# Configurações
TELEGRAM_TOKEN = "8595595411:AAEv1B1jCb-Np9-epIUwdIhB9IXITBb4xps"
GEMINI_KEY = "AIzaSyCAtlpoewdAMGeYnH-tjrg6bfxXDLLFdm0"

genai.configure(api_key=GEMINI_KEY)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

def get_working_model():
    # Esta função garante que pegamos o modelo disponível na sua conta
    modelos = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    return genai.GenerativeModel(model_name=modelos[0])

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        model = get_working_model()
        response = model.generate_content(message.text)
        resposta_final = response.text
        
        # Extração de código
        code_blocks = re.findall(r'```python\s+(.*?)\s+```', resposta_final, re.DOTALL)
        
        for i, code in enumerate(code_blocks):
            # Tenta pegar o nome do arquivo no comentário
            match = re.search(r'# Nome do arquivo:\s+([\w\.-]+)', code)
            filename = match.group(1) if match else f"script_gerado_{i}.py"
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(code)
            bot.reply_to(message, f"💾 Arquivo `{filename}` gravado com sucesso!")
        
        # Resposta de texto (limitada para não travar o Telegram)
        bot.reply_to(message, resposta_final[:4000])
            
    except Exception as e:
        bot.reply_to(message, f"Erro no Agente: {e}")

print("ROBLab Agente Reconfigurado e Online...")
bot.polling()