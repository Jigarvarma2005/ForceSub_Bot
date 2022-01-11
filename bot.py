import logging
from pyrogram import Client, idle
from Config import Config

plugins = dict(
        root="plugins"
         )

app = Client(
     'ForceSubscribeRobot',
      bot_token = Config.BOT_TOKEN,
      api_id = Config.APP_ID,
      api_hash = Config.API_HASH,
      plugins=plugins
)

app.start()
idle()
app.stop()