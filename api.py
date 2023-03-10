from streambotapi import StreamBotAPI
from streambot import StreamBot
import constants
import os

#Prompt 0 - Listing Bot
streambot1 = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt=constants.OPENAI_PROMPT[0])

#Prompt 1 - Neighborhood Bot
streambot2 = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt=constants.OPENAI_PROMPT[1])

server = StreamBotAPI([streambot1,streambot2], origins=["http://localhost:3000","https://paisley-ui-hycvm.ondigitalocean.app"], verbosity=1)

server.start()