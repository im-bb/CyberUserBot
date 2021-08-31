from os import environ
from pyrogram import Client, idle

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
session_name = environ["SESSION_NAME"]

plugins = dict(
    root="plugins",
    include=[
        "modules." + environ["PLUGIN"],
        "ping",
        "sysinfo"
    ]
)

app = Client(session_name, api_id, api_hash, plugins=plugins)
app.start()
print('CYBER aktivdir..')
idle()
app.stop()
