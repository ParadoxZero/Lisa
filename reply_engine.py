from chatterbot import ChatBot
import chatterbot

'''
chatbot = ChatBot("Lisa",database="../data.db")

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Train based on english greetings corpus
chatbot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
chatbot.train("chatterbot.corpus.english.conversations")

# Get a response to an input statement
while True :
	d = raw_input()
	chatbot.get_response(d)
'''

class reply_engine :
	bot = None
	def init(self):
		self.bot = ChatBot("Lisa",
		    storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
		    logic_adapter="chatterbot.adapters.logic.ClosestMatchAdapter",
		    io_adapter="chatterbot.adapters.io.NoOutputAdapter",
		    database="../database.db")
		self.bot.train(
    		"chatterbot.corpus.english"
)
	def get_reply(self,data):
		return self.bot.get_response(data)


if __name__ == "__main__":
	r = reply_engine()
	r.init()
	print r.get_reply("hello")
