# Copyright (C) 2021 FaridDadashzade.
#
# CyberUserBot - @faridxz

""" CYBERUSERBOT """

import sys
from asyncio import create_subprocess_shell as asyncsubshell
from asyncio import subprocess as asyncsub
from os import remove
from time import gmtime, strftime
from pathlib import Path
import re
import inspect
from traceback import format_exc

from telethon import events

from userbot import bot, BOTLOG_CHATID, CYBER_VERSION, LOGSPAMMER, PATTERNS, JARVIS, MYID


def register(**args):
    #stack = inspect.stack()
    #cyber_stack_frame = stack[1]
    #file_test = Path(cyber_stack_frame.filename)
    #file_test = file_test.stem.replace(".py", "")
    pattern = args.get('pattern', None)
    disable_edited = args.get('disable_edited', False)
    groups_only = args.get('groups_only', False)
    insecure = args.get("insecure", False)
    cyber = args.get('cyber', False)
    jarvis = args.get('jarvis', False)
    trigger_on_fwd = args.get('trigger_on_fwd', False)
    trigger_on_inline = args.get('trigger_on_inline', False)
    disable_errors = args.get('disable_errors', False)

    if pattern:
        args["pattern"] = pattern.replace("^.", "^["+ PATTERNS + "]")
    if "disable_edited" in args:
        del args['disable_edited']

    if "ignore_unsafe" in args:
        del args['ignore_unsafe']

    if "groups_only" in args:
        del args['groups_only']
    
    if "insecure" in args:
        del args["insecure"]  

    if "disable_errors" in args:
        del args['disable_errors']

    if "trigger_on_fwd" in args:
        del args['trigger_on_fwd']
      
    if "trigger_on_inline" in args:
        del args['trigger_on_inline']
        
    if 'cyber' in args:
        del args['cyber']
        args['outgoing'] = True      
        
    if 'jarvis' in args:
        del args['jarvis']
        args['incoming'] = True
        args["from_users"] = JARVIS
        

    def decorator(func):
        async def wrapper(check):
            if not LOGSPAMMER:
                send_to = check.chat_id
            else:
                send_to = BOTLOG_CHATID

            if not trigger_on_fwd and check.fwd_from:
                return

            if check.via_bot_id and not trigger_on_inline:
                return
             
            if groups_only and not check.is_group:
                await check.respond("`Bunun bir qrup olduğunu düşünmürəm!`")
                return

            try:
                await func(check)
                

            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except BaseException:
                if not disable_errors:
                    date = strftime("%d-%m-%Y", gmtime())

                    eventtext = str(check.text)
                    xetametni = str(sys.exc_info()[1])
                    text = "**CYBΞR ERROR LOG**\n"
                    link = "[CYBΞR Dəstək Qrupuna](https://t.me/TheCyberSupport)"
                    if len(eventtext)<10:
                        text += f"\n**⚙ Səbəb:** {eventtext}\n"
                    text += "\n🔸️ İstəsəniz bunu bizə bildirə bilərsiniz."
                    text += f" Sadəcə bu mesajı {link} göndərin.\n"
                    text += "Xəta və tarix xaricində heç bir şey qeyd edilmir.\n"

                    ftext = "========== XEBERDARLIQ =========="
                    ftext += "\nBu fayl sadəcə bura yüklənib,"
                    ftext += "\nSadəcə xəta və tarixi qeyd edirik,"
                    ftext += "\nGizliliyiniz bizim üçün önəmlidir,"
                    ftext += "\nBurada hər hansı bir gizli məlumat olarsa"
                    ftext += "\nBu xəta bildirişi olmaz, heç kəs sizin məlumatlarınızı oğurlaya bilməz.\n"
                    ftext += "--------USERBOT XƏTA LOG--------\n"
                    ftext += "\nTarix: " + date
                    ftext += "\nQrup ID: " + str(check.chat_id)
                    ftext += "\nGöndərən adamın ID: " + str(check.sender_id)
                    ftext += "\n\nƏmr:\n"
                    ftext += str(check.text)
                    ftext += "\n\nXəta mətni:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n\nDaha ətraflı:\n"
                    ftext += str(format_exc())
                    ftext += "\n\n--------USERBOT XETA LOGU SON--------"
                    ftext += "\n\n================================\n"
                    ftext += f"====== ⚠️ Version : {CYBER_VERSION} ======\n"
                    ftext += "================================"

                    command = "git log --pretty=format:\"%an: %s\" -5"

                    ftext += "\n\n\nSon 5 dəyişiklik:\n"

                    process = await asyncsubshell(command,
                                                  stdout=asyncsub.PIPE,
                                                  stderr=asyncsub.PIPE)
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) \
                        + str(stderr.decode().strip())

                    ftext += result

                    file = open("cyber.log", "w+")
                    file.write(ftext)
                    file.close()

                    if LOGSPAMMER:
                        try:
                            await check.client.send_message(check.chat_id, f"**{xetametni}**\n\n⌚️ **Tarix:** `{date}`\n\n❗️ **Əmr:** `{eventtext}`\n\n✅ **Xəta faylını** `BOTLOG` **qrupunuza göndərdim!**\n\n__CYBΞR ERROR LOG__")
                        except:
                            pass
                    await check.client.send_file(send_to,
                                                 "cyber.log",
                                                 caption=text)

                    remove("cyber.log")
            else:
                pass
        if not disable_edited:
            bot.add_event_handler(wrapper, events.MessageEdited(**args))
        bot.add_event_handler(wrapper, events.NewMessage(**args))

        return wrapper

    return decorator
