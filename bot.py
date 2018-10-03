from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import api

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
				level=logging.INFO)

logger = logging.getLogger(__name__)

Studio_Albums = ["In the Court of the Crimson King", "In the Wake of Poseidon", "Lizard", "Islands", "Lark's Tongues in Aspic", "Starless and Bible Black", "Red", "Discipline",
"Beat", "Three of a Perfect Pair", "THRAK", "the construKction of light", "The Power to Believe"]

Live_Albums = ["Earthbound", "USA", "B'Boom", "Thrakattak", "Absent Lovers", "The ProjeKcts", "Heavy ConstruKction", "Vrooom Vrooom", 
"EleKtrik", "Radical Action to Unseat the Hold of Monkey Mind", "Eyes Wide Open"]

EPs = ["Vrooom", "Level Five", "Happy with What You Have to Be Happy With", "Heroes", "Uncertain Times"]

Songs = ["21st Century Schizoid Man", "I Talk to the Wind", "Epitaph", "Moonchild", "The Court of the Crimson King", "Peace - A Beginning", "Pictures of a City", "Cadence and Cascade", 
"In the Wake of Poseidon", "Peace - A Theme", "Cat Food", "The Devil's Triangle", "Peace - An End", "Groon", "Cirkus", "Indoor Games", "Happy Family", "Lady of the Dancing Water", 
"Bolero", "Formentera Lady", "Sailor's Tale", "The Letters", "Ladies of the Road", "Prelude: Song of the Gulls", "Untitled", "Drop In", "A Peace Making Stint Unrolls", "Book of Saturday",
"Lark's Tongues in Aspic, Part One", "Exiles", "Easy Money", "The Talking Drum", "Lark's Tongues in Aspic, Part Two", "The Rich Tapestry of Life", "Zoom", "Zoom Zoom", "Z'Zoom", 
"Vista Training College Under Spotlight", "Fallen Angel Hullabaloo", "All That Glitters Is Not Nail Polish", "A Deniable Bloodline", "A Boolean Melody Medley", "A Vinyl Hobby Job", 
"Behold! Blond Bedlam", "An Edible Bovine Dynamo", "Ahoy! Modal Mania", "Keep That One, Nick", "Yeah a Vile Limey Body", "Abominable Ballyhoo", "The Great Deceiver", "Lament", 
"We'll Let You Know", "The Night Watch", "Trio", "The Mincer", "Fracture", "Fallen Angel", "One More Red Nightmare", "Providence", "Starless", "A Voyage to the Centre of the Cosmos", 
"Improv I", "Improv II", "Bartley Butsford", "Daniel Dust", "Wilton Carpet", "The Golden Walnut", "Clueless and Slightly Slack", "Asbury Park", "It is for You, but Not for Us", "Cerberus", 
"Elephant Talk", "Frame by Frame", "Matte Kudasai", "待ってください", "Please Wait for Me", "Indiscipline", "Thela Hun Ginjeet", "The Sheltering Sky", "Neal and Jack and Me", "Heartbeat", 
"Sartori in Tangier", "Waiting Man", "Neurotica", "Two Hands", "The Howler", "Requiem", "Three of a Perfect Pair", "Model Man", "Sleepless", "Man with an Open Heart", "Nuages", 
"Industry", "Dig Me", "No Warning", "Larks' Tongues in Aspic (Part III)", "Industrial Zone A", "Industrial Zone B", "The King Crimson Barber Shop", "Shidare Zakura", "Industrial Zone C", 
"Coda: Marine 475", "Dinosaur", "Walking on Air", "Inner Garden I", "People", "Radio I", "One Time", "Radio II", "Inner Garden II", "Sex Sleep Eat Drink Dream" "When I Say Stop, Continue", 
"Cage", "Funky Jam", "Krim 3", "Bass Groove", "Calliope", "No Questions Asked", "Monster Jam", "Fans, Sloth, Nuns, Felons", "Declamatory Doth Madden", "Witnessing Dumb Whodunnits", 
"Cloudscape", "Jimmy Bond", "Sad Woman Jam", "Tony's Jam", "Silent Night à la Frippertronics", "Entry of the Crims", "Two Sticks", "Prism", "Conundrum", "Fearless and Highly THRaKked", 
"Free as a Bird", "Biker Babes of the Rio Grande", "Mother Hold the Candle Steady While I Shave the Chicken's Lip", "The Slaughter of the Innocents", "This Night Wounds Time", "The Race",
"Dressing Room", "Tokyo", "From the Hotel", "Mr. Bill at the Station", "ProzaKc Blues", "Into the Frying Pan", "FraKctured", "The World's My Oyster Soup Kitchen Floor Wax Museum", 
"Larks' Tongues in Aspic – Part IV", "Coda: I Have a Dream", "Heaven and Earth", "Mastelotticus SS Blasticus", "The Power to Believe I: A Cappella", "Facts of Life", "The Power to Believe II: Power Circle", 
"Dangerous Curves", "The Power to Believe III: Deception of the Thrush", "The Power to Believe IV: Coda"]

Members = ["Robert Fripp", "Mel Collins", "Tony Levin", "Pat Mastelotto", "Gavin Harrison", "Jakko Jakszyk", "Bill Rieflin", "Jeremy Stacey", "Michael Giles", "Ian McDonald", "Peter Sinfield", 
"Greg Lake", "Gordon Haskell", "Andy McCulloch", "Ian Wallace", "Boz Burrell", "John Wetton", "Jamie Muir", "Bill Bruford", "David Cross", "Adrian Belew", "Trey Gunn", "Chris Gibson"]

Misc = ["King Crimson", "(no pussyfooting)", "Frippertronics"]

DGM_Live = Studio_Albums.append(Songs.append(Members.append(Misc.append(Live_Albums.append(EPs)))))

def start(bot, update):
	update.message.reply_text("I am now monitoring this chat")

def help(bot, update):
	update.message.reply_text("Do not worry, I am here now")

def dev(bot, update):
	update.message.reply_text("Greetings, my name is Robot Fripp. I am a robot that was developed by Rafael Dulfer to make sure DGM Live's intellectual property stays protected, even on telegram. If you have any suggestions, you can provide them on Github https://github.com/Rafaeltheraven/FrippBot")

def error(bot, update, error):
	logger.warning('Update "%s" caused error "%s"', update, error)

def physical_media(bot, update):
	text = update.message.text
	user = update.message.from_user
	for intellectual_property in DGM_Live:
		if intellectual_property.lower() in text.lower():
			bot.send_sticker(chat_id=update.message.chat_id, sticker="CAADBAADIQADWqa-IJq3Af2Tz1s6Ag", reply_to_message_id=update.message.message_id)
			bot.send_message(chat_id=update.message.chat_id, text=">" + intellectual_property + "\n You did buy my album, right " + user.first_name + "?")


def main():
	updater = Updater(api.get_key())
	dp = updater.dispatcher
	dp.add_handler(MessageHandler(Filters.text, physical_media))
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(CommandHandler("dev", dev))
	dp.add_error_handler(error)
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()