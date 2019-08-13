from telegram.ext import Updater
from .secret import secret_token

updater = Updater(secret_token, use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

from collections import defaultdict
from telegram import ParseMode

def welcome_fun(update, context):
    additional_messages = defaultdict(lambda: "")
    additional_messages.update({
    -1001287088369: "Questa chat è dedicata a prendere appuntamento con i certificatori per finalizzare la tua adesione al partito pirata. Chiedi di loro e aspetta che rispondano. Una volta preso un appuntamento sarai rimoss@ da questa chat e aggiunto alle altre, se lo desideri.", # ppLounge
    -239595992: "Ciao, Cal.", # muahahah playground (a testing chat)
    -379858320: "Questa è la chat dei certificatori del partito pirata. Sei sicur@ di essere nel posto giusto?", # ppCertificatori
    -1001071747041: "La Tolda dei Pirati è un luogo di discussione libera e senza particolari vincoli, ed *è un gruppo pubblico*. Nel caso ti interessino, ci sono anche dei gruppi Telegram locali, <a href=\"https://wiki.partito-pirata.it/Telegram\">elencati nella wiki</a>."
    })

    chat_id = update.message.chat_id
    for user in update.message.new_chat_members:
        params = {
        "chat_name": update.message.chat.title,
        "user": user.first_name,
        "additional_message": additional_messages[chat_id]
        }
        text = "Benvenut@ in {chat_name}, <b>{user}</b>. {additional_message}".format(**params)
        context.bot.send_message(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)

def help_fun(update, context):
    non_ho_capito = "Non ho capito. Per conoscere gli argomenti disponibili, invoca /help"
    topic = defaultdict(lambda: non_ho_capito)
    topic.update({
        "lqfb": "LiquidFeedback è un software che gestisce le mozioni politiche del partito.\n\nPiù informazioni qui: https://www.partito-pirata.it/DocumentazioneLQFB/",
        "babele": "Babele, il più fico del paniere.",
        "solibo": "Solibo è una gran testa. Di cazzo.",
        "ramarr0": "aggiungimi alla lista dei topic per cortesia, scrivendo che sono una gran testa di cazzo.",
        "cal": "Cal non è qui",
        "pagamenti": "Il tuo certificatore dovrebbe averti comunicato l'ammontare della quota, le coordinate per il pagamento sono su questa pagina: https://www.partito-pirata.it/donazioni/",
        "sorgente": "https://github.com/PartitoPirata/CertificatoreBot"
    })

    try:
        risposta = topic[update.message.text.split()[1]]
    except IndexError:
        risposta = "Ciao, sono un bot che può risponderti su alcuni argomenti. Gli argomenti disponibili sono: {}.\n\nChiedi con /help argomento".format(', '.join(sorted(topic)))

    context.bot.send_message(chat_id=update.message.chat_id,
    text=risposta, parse_mode=ParseMode.MARKDOWN)



from telegram.ext import CommandHandler, MessageHandler, Filters

dispatcher.add_handler(CommandHandler('help', help_fun))
dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome_fun))
