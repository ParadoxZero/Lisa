'''


This is the part where program communicates with the chat bot.This module wont work unless the dependent packages are installed.
replace xxxx with tier 1 module and funct_ with function name.


The following have to be included in tier_3


import tier_2

while True:
    try: print tier_2.bot_com()
    except (KeyboardInterrupt, EOFError, SystemExit):
        break




'''

from chatterbot import ChatBot
import xxxx
import os


bot = ChatBot("Terminal",
    storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
    logic_adapter="chatterbot.adapters.logic.ClosestMatchAdapter",
    io_adapter="chatterbot.adapters.io.TerminalAdapter",
    database="../database.db")



def bot_com():
 
        '''
        ChatterBot's get_input method uses io adapter to get new input for
        the bot to respond to. In this example, the TerminalAdapter gets the
        input from the user's terminal. Other io adapters might retrieve input
        differently, such as from various web APIs.
        But here I have used a function from previous tier to feed input to the bot.
        '''
        funt_input = xxxx.funct_()

        '''
        The get_response method also uses the io adapter to determine how
        the bot's output should be returned. In the case of the TerminalAdapter,
        the output is printed to the user's terminal.But this output is redundent and I have cleared it.But this destroys the  previous contents in console.This has to be considered while creating the interface.
        '''
        bot_output = bot.get_response(funct_input)
        os.system('clear')
        
        return bot_output
    
