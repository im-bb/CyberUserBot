----

<p align="center"><a href="https://t.me/TheCyberUserBot"><img src="https://telegra.ph/file/2b7c70f6a262e6bbd41ad.jpg" width="600"></a></p> 
<h1 align="center"><b>C Y B Ξ R USΣRBOT 🇦🇿</b></h1>
</div>
<p align="center">
    C Y B Ξ R UserBot, Telegram istifadəsini asanlaşdıran bir proyektdir. Müəllif hüquqları MIT Licence ilə qorunur.
    
</p>

----

## Qurulum

### Avtomatik Qurulum

**Android:** Termuxu açın və bu kodu yapışdırın: `bash <(curl -L https://bit.ly/2SuGkcA)`

**iOS:** iSH açın ve bu kodu yapışdırın: `apk update && apk add bash && apk add curl && curl -L -o cyber_installer.sh https://git.io/JYKsg && chmod +x cyber_installer.sh && bash cyber_installer.sh`

**Windows** `Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://git.io/JOHQ2')`

## Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/im-bb/CyberUserBot)

### Çətin Yol
```python
git clone https://github.com/FaridDadashzade/CyberUserBot.git
cd CyberUserBot
pip install -r requirements.txt
# Config.env yaradın və düzəldin. #
python3 main.py
```

## String Session

[![Run on Repl.it](https://repl.it/badge/github/FaridDadashzade/Cyber)](https://repl.it/@FaridDadashzade/Cyber)

## Nümunə Plugin
```python
from userbot.events import register
from userbot.cmdhelp import CmdHelp 
# <-- Bunlar mütləq olmalıdır

@register(outgoing=True, pattern="^.test")
async def test(event):
    await event.edit('C Y B Ξ R UserBot')

Help = CmdHelp('test') # Məlumat yazacıq.
Help.add_command('test', # Əmri bu şəkildə yazırıq.
    None,
    'Test edir', # Bura isə əmrin açıqlamasını yazırıq.
    'test'
    )
Help.add_info('@faridxz tərəfindən hazırlanmışdır.') # Bu şəkildə məlumat yaza bilərsiniz.
Help.add_warning('Xəbərdarlıq mesajı') # Burayada xəbərdarlıq mesajı yazırıq.
Help.add()
```



## Qeyd
```
    UserBot ilə əlaqəli; Telegram hesabınız bağlana bilər.
    Bu bir açıq qaynaqlı proyektdir, CYBΞR Sahibləri və Adminləri olaraq heç bir cavabdehlik daşımırıq.
    CYBΞR quraraq bu cavabdehlikləri qəbul etmiş sayılırsınız.
```

----
#### i'm not a dev,just edited somelines of this repo to make it easy to understand-Translated some lines into English.
<p align="center">
  <img src="https://telegra.ph/file/1e464be45f761a810643b.png" />
</p>

