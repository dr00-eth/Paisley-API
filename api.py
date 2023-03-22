from streambotapi import StreamBotAPI
from streambot import StreamBot
import constants
import os
import logging

openaikey = os.getenv('OPENAI_KEY')

#Prompt 0 - Listing Bot
streambot1 = StreamBot(openaikey, "Paisley", genesis_prompt=constants.OPENAI_PROMPT[0])

#Prompt 1 - Neighborhood Bot
streambot2 = StreamBot(openaikey, "Paisley", genesis_prompt=constants.OPENAI_PROMPT[1])

#Prompt 2 - Coaching Bot
streambot3 = StreamBot(openaikey, "Paisley", genesis_prompt=constants.OPENAI_PROMPT[2])

#Prompt 3 - Follow Up Bot
streambot4 = StreamBot(openaikey, "Paisley", genesis_prompt=constants.OPENAI_PROMPT[3])

#Prompt 4 - ChatGPT Generic
streambot5 = StreamBot(openaikey, "Paisley", genesis_prompt=constants.OPENAI_PROMPT[4])

server = StreamBotAPI([streambot1,streambot2, streambot3, streambot4, streambot5], origins=["http://localhost:3000","https://paisley-ui-develop-arxkt.ondigitalocean.app","https://paisley-proto.thegenie.ai"], verbosity=1, debug=False, allow_model_override=True, port=443)

server.start()