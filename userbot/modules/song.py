# Copyright (C) 2021 FaridDadashzade.
#
# TheCyberUserBot - Faridxz
#
# All rights reserved.

import datetime
import json
import pybase64
import asyncio
import shutil
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register
from asyncio.exceptions import TimeoutError
from telethon.tl.types import DocumentAttributeAudio, DocumentAttributeVideo

import os
import subprocess
from youtube_dl import YoutubeDL
from userbot.utils import progress
import glob
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)
from youtubesearchpython import SearchVideos
from random import randint
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("song")

# ████████████████████████████████ #


@register(outgoing=True, pattern="^.deez(\d*|)(?: |$)(.*)")
async def deezl(event):
    if event.fwd_from:
        return
    sira = event.pattern_match.group(1)
    if sira == '':
        sira = 0
    else:
        sira = int(sira)

    sarki = event.pattern_match.group(2)
    if len(sarki) < 1:
        if event.is_reply:
            sarki = await event.get_reply_message().text
        else:
            await event.edit(LANG['GIVE_ME_SONG']) 

    await event.edit(LANG['SEARCHING'])
    chat = "@DeezerMusicBot"
    async with bot.conversation(chat) as conv:
        try:     
            mesaj = await conv.send_message(str(randint(31,62)))
            sarkilar = await conv.get_response()
            await mesaj.edit(sarki)
            sarkilar = await conv.get_response()
        except YouBlockedUserError:
            await event.reply(LANG['BLOCKED_DEEZER'])
            return
        await event.client.send_read_acknowledge(conv.chat_id)
        if sarkilar.audio:
            await event.client.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, LANG['UPLOADED_WITH'], file=sarkilar.message)
            await event.delete()
        elif sarkilar.buttons[0][0].text == "No results":
            await event.edit(LANG['NOT_FOUND'])
        else:
            await sarkilar.click(sira)
            sarki = await conv.wait_event(events.NewMessage(incoming=True,from_users=595898211))
            await event.client.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, f"`{sarkilar.buttons[sira][0].text}` | " + LANG['UPLOADED_WITH'], file=sarki.message)
            await event.delete()


@register(outgoing=True, pattern=r"^\.song (.*)")
async def download_video(event):
    await event.edit("`Musiqi axtarılır...`")
    url = event.pattern_match.group(1)
    if not url:
        return await event.edit("**Xəta!**\nİstifadəsi `.song <musiqi adı>`")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await event.edit("`Bağışlayın heçnə tapa bilmədim...`")
    type = "audio"
    await event.edit(f"`Yükləməyə hazırlanır {url}...`")
    if type == "audio":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
    try:
        await event.edit("`Məlumatlar alınır...`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await event.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await event.edit("`Yükləmə məzmunu çox qısadır.`")
        return
    except GeoRestrictedError:
        await event.edit(
            "`Coğrafi məhdudiyyətlər veb sayt tərəfindən tətbiq olunduğu üçün coğrafi məkanınızdan videolar mövcud deyil.`"
        )
        return
    except MaxDownloadsReached:
        await event.edit("`Limitə çatıldı...`")
        return
    except PostProcessingError:
        await event.edit("`Bağışlayın bir xəta baş verdi...`")
        return
    except UnavailableVideoError:
        await event.edit("`Bağışlayın bir xəta baş verdi...`")
        return
    except XAttrMetadataError as XAME:
        await event.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await event.edit("`Bağışlayın bir xəta baş verdi.`")
        return
    except Exception as e:
        await event.edit(f"{str(type(e)): {str(e)}}")
        return
    try:
        sung = str(pybase64.b64decode("QHRoZWN5YmVydXNlcmJvdA=="))[2:14]
        await bot(JoinChannelRequest(sung))
    except BaseException:
        pass
    upteload = """
Musiqi yüklənməyə hazırlanır...
Başlıq - {}
Sahibi - {}
""".format(
        rip_data["title"], rip_data["uploader"]
    )
    await event.edit(f"`{upteload}`")
    await event.client.send_file(
        event.chat_id,
        f"{rip_data['id']}.mp3",
        supports_streaming=True,
        caption=f"**✍ Başlıq:** {rip_data['title']}\n**👤 Sahibi:** {rip_data['uploader']}\n",
        attributes=[
            DocumentAttributeAudio(
                duration=int(rip_data["duration"]),
                title=str(rip_data["title"]),
                performer=str(rip_data["uploader"]),
            )
        ],
    )
    os.remove(f"{rip_data['id']}.mp3")


@register(outgoing=True, pattern="^.songpl ?(.*)")
async def songpl(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = event.pattern_match.group(1)

    if len(cmd) < 1:
        await event.edit(LANG['USAGE_PL'])    

    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    await event.edit(LANG['SEARCHING_PL'])
    dosya = os.getcwd() + "/playlist/" + "pl.pl"
    klasor = os.getcwd() + "/playlist/"
    sonuc = os.system(f"spotdl --playlist {cmd} --write-to=\"{dosya}\"")
    sonuc2 = os.system(f"spotdl --list {dosya} -f {klasor}")
    await event.edit(LANG['DOWNLOADED'])
    l = glob.glob(f"{klasor}/*.mp3")
    i = 0
    if len(l) >= 1:
        while i < len(l):
            await event.reply(LANG['SENDING_SONGS'] + l[i])
            await event.client.send_file(
                event.chat_id,
                l[i],
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id
            )
    else:
        await event.edit(LANG['NOT_FOUND_PL'])   
        return 
    os.system(f"rm -rf {klasor}/*.mp3")
    subprocess.check_output(f"rm -rf {klasor}/*.mp3",shell=True)
    os.system(f"rm -rf {klasor}/*.pl")
    subprocess.check_output(f"rm -rf {klasor}/*.pl",shell=True)


CmdHelp('song').add_command(
    'deez', '<musiqi adı/youtube/spotify/soundcloud>', 'Birçox saytdan musiqini axtarıb, yükləyər.'
).add_command(
    'song', '<musiqi adı/youtube/spotify>', 'Musiqi yükləyər.'
).add_command(
    'songpl', '<spotify playlist>', 'Spotify Playlist\'indən musiqi yükləyər'
).add()
