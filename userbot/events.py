# Copyright (C) 2021 FaridDadashzade.
#
# CyberUserBot - @faridxz

""" CYBERUSERBOT """

import sys
from asyncio import create_subprocess_shell as asyncsubshell
from asyncio import subprocess as asyncsub
from os import remove
from time import gmtime, strftime
from traceback import format_exc

from telethon import events

from userbot import bot, BOTLOG_CHATID, CYBER_VERSION, LOGSPAMMER, PATTERNS, JARVIS, MYID


def register(**args):
    """ Yeni bir etkinlik qeyd edin. """
    pattern = args.get('pattern', None)
    disable_edited = args.get('disable_edited', False)
    groups_only = args.get('groups_only', False)
    insecure = args.get("insecure", False)
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
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    eventtext = str(check.text)
                    xetatext = str(sys.exc_info()[1])
                    ftext += "\n\nƏmr:\n"
                    ftext += str(check.text)
                    ftext += "\n\nXəta mətni:\n"
                    ftext += str(sys.exc_info()[1])
                    
                    if LOGSPAMMER:
                        try:
                            await check.edit("`Bağışlayın,\n ℹ️ Xəta günlükləri UserBot günlük qrupunda saxlanılır.`")
                        except:
                            pass
                    await client.send_message(xetatext)

            else:
                pass
        if not disable_edited:
            bot.add_event_handler(wrapper, events.MessageEdited(**args))
        bot.add_event_handler(wrapper, events.NewMessage(**args))

        return wrapper

    return decorator
