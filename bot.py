from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
				level=logging.INFO)

logger = logging.getLogger(__name__)

DGM_Live = ["King Crimson", "Robert Fripp", "In the Court of the Crimson King", "In the Wake of Poseidon", "Lizard", "Islands", "Lark's Tongues in Aspic", "Starless and Bible Black", "Red", "Discipline",
"Beat", "Three of a Perfect Pair", "THRAK", "the construKction of light", "The Power to Believe", "Earthbound", "USA", "The Great Deceiver", "B'Boom", "Thrakattak", "Epitaph", "The Night Watch", 
"Absent Lovers", "The ProjeKcts", "Heavy ConstruKction", "Vrooom Vrooom", "Ladies of the Road", "EleKtrik", "Radical Action to Unseat the Hold of Monkey Mind", "Vrooom", "Level Five", 
"Happy with What You Have to Be Happy With", "Heroes", "Uncertain Times"]

def start(bot, update):
	update.message.reply_text("I am now monitoring this chat")

def help(bot, update):
	update.message.reply_text("Do not worry, I am here now")

def error(bot, update, error):
	logger.warning('Update "%s" caused error "%s"', update, error)

def physical_media(bot, update):
	text = update.message.text
	user = update.message.from_user
	for intellectual_property in DGM_Live:
		if intellectual_property.lower() in text.lower():
			bot.send_sticker(chat_id=update.message.chat_id, sticker="CAADBAADIQADWqa-IJq3Af2Tz1s6Ag", reply_to_message_id=update.message.message_id)
			bot.send_message(chat_id=update.message.chat_id, text="You did buy my album, right " + user.first_name + "?")


def main():
	updater = Updater("670227068:AAFh8vI8Svv9IdK51wqv9FEjTlbylqLZKa0")
	dp = updater.dispatcher
	dp.add_handler(MessageHandler(Filters.text, physical_media))
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	dp.add_error_handler(error)
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()