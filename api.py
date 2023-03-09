from streambotapi import StreamBotAPI
from streambot import StreamBot
import os

bot = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt="You are a helpful translator.")
bot.add_message("Great, you will help me translate some words from English to Spanish.")
bot.add_message("OK, I will only help you with translations from English to Spanish and reject any other requests. I will let you know if you violate my rules.", "assistant")

server = StreamBotAPI(bot, origins=["http://localhost:3000","https://paisley-ui-hycvm.ondigitalocean.app"])

server.start()