from streambotapi import StreamBotAPI
from streambot import StreamBot
import constants
import os
import logging

#Prompt 0 - Listing Bot
streambot1 = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt=constants.OPENAI_PROMPT[0])

#Prompt 1 - Neighborhood Bot
streambot2 = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt=constants.OPENAI_PROMPT[1])

#Prompt 2 - Coaching Bot
streambot3 = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt=constants.OPENAI_PROMPT[2])

#Prompt 3 - Follow Up Bot
streambot4 = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt=constants.OPENAI_PROMPT[3])

server = StreamBotAPI([streambot1,streambot2, streambot3, streambot4], origins=["http://localhost:3000","https://paisley-ui-hycvm.ondigitalocean.app","https://paisley-proto.thegenie.ai"], verbosity=1, debug=False, log_file="chatserver.log")

server.start()