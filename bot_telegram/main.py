import telebot
from dotenv import load_dotenv
import os

# Configuração de autenticação
load_dotenv()
key = os.getenv('CHAVE_API')
bot = telebot.TeleBot(key)

# Comandos
@bot.message_handler(commands=['pizza','hamburger','salada'])
def menu(message):
    text = f'Seu pedido de {message.text[1:]} foi solicitado.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['opcao1'])
def opcao1(message):
    text = """
    O que você deseja? (Clique na opção)
    /pizza Pizza
    /hamburger Hamburger
    /salada Salada
    """
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['opcao2'])
def opcao2(message):
    bot.send_message(message.chat.id, 'Para enviar uma reclamação, mande um email para reclamacao@email.com')

@bot.message_handler(commands=['opcao3'])
def opcao3(message):
    bot.send_message(message.chat.id, 'Obg, um abraço tbm.')


# Mensagem padrão
def verify(message):
    return True

@bot.message_handler(func=verify)
def default_reply(message):
    text = """
    Escolha uma opção para continuar (Clique no item):
        /opcao1 Fazer um pedido
        /opcao2 Reclamar de um pedido
        /opcao3 Mandar um abraço
        Responder qualquer outra coisa não funcionará, clique em uma das opções.
    """
    bot.reply_to(message, text)

# Loop do bot
bot.polling()