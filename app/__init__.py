from telegram.ext import Updater
from .secret import secret_token

updater = Updater(secret_token, use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def welcome_fun(update, context):
    chat_id = update.message.chat_id
    for user in update.message.new_chat_members:
        text = "Benvenuto in ppLounge, {}. Questa chat è dedicata a prendere appuntamento con i certificatori per finalizzare la tua adesione al partito pirata. Chiedi di loro e aspetta che rispondano. Una volta preso un appuntamento sarai rimosso da questa chat e aggiunto alle altre, se lo desideri.".format(user.first_name)
        context.bot.send_message(chat_id=chat_id, text=text)

def help_fun(update, context):
    topic = {
        "lince": "Wovon man nicht sprechen kann, darüber muß man schweigen.",
        "lqfb": "È troppo presto per parlarne, ma è un software che gestisce le mozioni politiche del partito.",
        "babele": "babele è il più fico di tutti",
        "solibo": "aspetta il deploy",
        "cal": "Cal non è qui",
        "tesoreria": "Il tuo certificatore dovrebbe averti comunicato l'ammontare della quota, le coordinate per il pagamento sono su questa pagina: https://www.partito-pirata.it/donazioni/"
    }

    try:
        argomento = update.message.text.split()[1]

        if argomento in topic:
            risposta = topic[argomento]
        else:
            risposta = "Non ho capito. Per conoscere gli argomenti disponibili, invoca /help"
    except IndexError:
        risposta = "Ciao, sono un bot che può risponderti su alcuni argomenti. Gli argomenti disponibili sono: {}.\n\nChiedi con /help argomento".format(', '.join(topic))

    context.bot.send_message(chat_id=update.message.chat_id,
                             text=risposta)



from telegram.ext import CommandHandler, MessageHandler, Filters

dispatcher.add_handler(CommandHandler('help', help_fun))
dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome_fun))
