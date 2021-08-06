# CYBERUSERBOT 2021 (C)
#
# Cooming soon

class Text:
    nece = "`Bir mp3 faylına cavab verin və ya bir mahnı adı qeyd edin!`"
    admin_deyilsen = "`Bunu etmək üçün icazəniz yoxdur!`"
    yukle = "`Yüklənir...`"
    yardim = """
**Available Commands:**\n
  - `{x}alive` - __asistanın aktiv olub olmadığını yoxlayın.__
  - `{x}seslendir <link/mp3-ə cavab>` - __musiqini səsləndirər.__
  - `{x}pauza` - __pauza edər.__
  - `{x}resume` - __musiqini davam etdirər.__
  - `{x}song <mahnı adı>` - __musiqini yükləyər.__
**CYBER USERBOT**"""


    
async def mahniniseslendir(pycalls, message, song):
    try:
        await pycalls.stream(message.chat.id, song)
    except Exception as e:
        await message.reply_text(f"Səsləndirilə bilmədi!\n\nXəta:\n{e}")
