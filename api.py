from streambotapi import StreamBotAPI
from streambot import StreamBot
import os

bot = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt="You are a helpful translator.")
bot.add_message("Great, you will help me translate some words from English to Spanish.")

server = StreamBotAPI(bot, origins=["http://localhost:3000","https://paisley-ui-hycvm.ondigitalocean.app"])

server.start()