from chatterbot import ChatBot




class reply_engine :
	bot = None
	def init(self):
		self.bot = ChatBot("Lisa",
		    storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
		    logic_adapter="chatterbot.adapters.logic.ClosestMatchAdapter",
		    io_adapter="chatterbot.adapters.io.NoOutputAdapter",
		    database="database/database.db")
	def get_reply(self,data):
		return self.bot.get_response(data)
	def train(self):
		trainingData = []
		print "Input Converstion"
		while True:
			data = raw_input()
			if data == "#":
				break
			trainingData.append(data)
		self.bot.train(trainingData)



if __name__ == "__main__":
	r = reply_engine()
	r.init()
	r.train()