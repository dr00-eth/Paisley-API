from streambotapi import StreamBotAPI
from streambot import StreamBot
import constants
import os
import logging

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler and set its level
file_handler = logging.FileHandler('chatserver.log')
file_handler.setLevel(logging.DEBUG)

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)

#Prompt 0 - Listing Bot
streambot1 = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt=constants.OPENAI_PROMPT[0])

#Prompt 1 - Neighborhood Bot
streambot2 = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt=constants.OPENAI_PROMPT[1])

server = StreamBotAPI([streambot1,streambot2], origins=["http://localhost:3000","https://paisley-ui-hycvm.ondigitalocean.app"], verbosity=1, log_file=logger)

server.start()