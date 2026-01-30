# Nome do arquivo: minerador_financeiro.py

import asyncio
import json
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError, ChannelInvalidError, UsernameInvalidError

# --- Configurações da API do Telegram ---
API_ID = 35528506
API_HASH = '8a606c12e676a2d066da387072a0c131'
SESSION_NAME = 'minerador_financeiro_session' # Nome para o arquivo de sessão (ex: minerador_financeiro_session.session)

# --- Configurações do Garimpo ---
CHANNEL_USERNAME = 'Dicas_Financeiras_Poupanca'
MESSAGE_LIMIT = 15
OUTPUT_FILE = 'noticias.json'

async def main():
    print("Iniciando minerador de notícias financeiras...")

    # Cria uma instância do cliente Telethon
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

    try:
        print("Conectando ao Telegram...")
        # Conecta o cliente. Se for a primeira vez, ele pedirá um número de telefone e código.
        await client.start()
        print("Conectado com sucesso ao Telegram!")

        print(f"Buscando as últimas {MESSAGE_LIMIT} mensagens do canal '{CHANNEL_USERNAME}'...")

        messages_data = []
        
        # Itera pelas mensagens do canal
        # O 'async for' é usado porque client.iter_messages é um gerador assíncrono
        async for message in client.iter_messages(CHANNEL_USERNAME, limit=MESSAGE_LIMIT):
            if message.text: # Garante que a mensagem tem conteúdo de texto
                messages_data.append({
                    'id': message.id,
                    'date': message.date.isoformat(), # Converte o objeto datetime para string ISO 8601
                    'text': message.text
                })
        
        print(f"Total de {len(messages_data)} mensagens com texto encontradas.")

        if messages_data:
            # Salva os dados em um arquivo JSON
            print(f"Salvando mensagens em '{OUTPUT_FILE}'...")
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                # Usa indent=4 para formatar o JSON de forma legível
                # ensure_ascii=False para permitir caracteres não-ASCII (como acentos) no JSON
                json.dump(messages_data, f, indent=4, ensure_ascii=False)
            print(f"Mensagens salvas com sucesso em '{OUTPUT_FILE}'.")
        else:
            print("Nenhuma mensagem com conteúdo de texto foi encontrada para salvar.")

    except SessionPasswordNeededError:
        print("AVISO: Senha de duas etapas necessária. Por favor, execute o script novamente e insira a senha.")
    except (ChannelInvalidError, UsernameInvalidError):
        print(f"ERRO: O canal '{CHANNEL_USERNAME}' não foi encontrado ou é inválido. Verifique o nome de usuário do canal.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        print("Desconectando do Telegram...")
        await client.disconnect()
        print("Desconectado.")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")