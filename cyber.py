from pyrogram import Client, idle

app = Client("cyber")
app.start()
print('CYBER Aktivdir...')
idle()
app.stop()
