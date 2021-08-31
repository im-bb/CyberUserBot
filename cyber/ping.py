from time import time
from datetime import datetime
from pyrogram import Client, filters, emoji
from pyrogram.types import Message

self_or_contact_filter = filters.create(
    lambda
    _,
    __,
    message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)

@Client.on_message(filters.text
                   & self_or_contact_filter
                   & ~filters.edited
                   & ~filters.via_bot
                   & filters.regex("^!ping$"))
async def ping_pong(_, m: Message):
    start = time()
    m_reply = await m.reply_text("Hesablanır...")
    delta_ping = time() - start
    await m_reply.edit_text(
        f"Pinginiz: `{delta_ping * 1000:.3f} ms`"
    )
