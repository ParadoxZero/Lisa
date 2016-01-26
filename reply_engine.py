from chatterbot import ChatBot




class reply_engine :
	bot = None
	def init(self):
		self.bot = ChatBot("Lisa",
		    storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
		    logic_adapter="chatterbot.adapters.logic.ClosestMatchAdapter",
		    io_adapter="chatterbot.adapters.io.NoOutputAdapter",
		    database="database/database.db")
		self.bot.train(
    		"chatterbot.corpus.english"
)
	def get_reply(self,data):
		return self.bot.get_response(data)


if __name__ == "__main__":
	r = reply_engine()
	r.init()
	print r.get_reply("hello")
