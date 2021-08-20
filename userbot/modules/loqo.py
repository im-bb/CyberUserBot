import glob
import os
import random

from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterPhotos
from userbot.events import register
from userbot import DEFAULT_NAME, SAHIB_ID
from userbot.cmdhelp import CmdHelp

# credits: https://github.com/TeamUltroid/Ultroid/blob/main/plugins/logo.py

@register(cyber=True, pattern=r"^\.loqo(?: |$)(.*)")
@register(cyber=True, pattern=r"^\.logo(?: |$)(.*)")
async def logo_gen(event):
    ad = event.pattern_match.group(1)
    name = event.pattern_match.group(1)
    if not ad:
        await event.edit("`Loqo hazırlaya bilməyim üçün bir ad verin!`")
    bg_, font_ = "", ""
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            if hasattr(temp.media, "document"):
                if "font" in temp.file.mime_type:
                    font_ = await temp.download_media()
                elif (".ttf" in temp.file.name) or (".otf" in temp.file.name):
                    font_ = await temp.download_media()
            elif "pic" in mediainfo(temp.media):
                bg_ = await temp.download_media()
    else:
        pics = []
        async for i in event.client.iter_messages(
            "@CyberLoqo", filter=InputMessagesFilterPhotos
        ):
            pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download_media()
        fpath_ = glob.glob("userbot/cyberfonts/*")
        font_ = random.choice(fpath_)
    if not bg_:
        pics = []
        async for i in event.client.iter_messages(
            "@CyberLoqo", filter=InputMessagesFilterPhotos
        ):
            pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download_media()
    if not font_:
        fpath_ = glob.glob("userbot/cyberfonts/*")
        font_ = random.choice(fpath_)
    if len(ad) <= 8:
        fnt_size = 150
        strke = 10
    elif len(ad) >= 9:
        fnt_size = 50
        strke = 5
    else:
        fnt_size = 130
        strke = 20
    img = Image.open(bg_)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_, fnt_size)
    w, h = draw.textsize(ad, font=font)
    h += int(h * 0.21)
    image_width, image_height = img.size
    draw.text(
        ((image_width - w) / 2, (image_height - h) / 2),
        ad,
        font=font,
        fill=(255, 255, 255),
    )
    x = (image_width - w) / 2
    y = (image_height - h) / 2
    draw.text(
        (x, y), ad, font=font, fill="white", stroke_width=strke, stroke_fill="black"
    )
    fayladi = f"cyber.png"
    img.save(fayladi, "png")
    await event.edit("`Hazırdır logo göndərilir...`")
    if os.path.exists(fayladi):
        await event.client.send_file(
            event.chat_id,
            file=fayladi,
            caption=f"[C Y B Ξ R](https://t.me/thecyberuserbot) [{DEFAULT_NAME}](tg://user?id={SAHIB_ID}) üçün logo hazırladı.",
            force_document=True,
        )
        os.remove(fayladi)
        await event.delete()
    if os.path.exists(bg_):
        os.remove(bg_)
    if os.path.exists(font_):
        if not font_.startswith("userbot/cyberfonts/"):
            os.remove(font_)

Help = CmdHelp('logo')
Help.add_command('logo', '<yazı>', 'C Y B Ξ R sizin üçün logo hazırlayar.')
Help.add_info('@TheCyberUserBot')
Help.add() 
