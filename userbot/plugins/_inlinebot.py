from math import ceil
from re import compile
import asyncio
import html
import os
import re
import sys
from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ExportChatInviteRequest
from . import *
from userbot.Config import Config
DEFAULTUSER = ALIVE_NAME or "PYTHON"
python_row = Config.BUTTONS_IN_HELP
python_emoji1 = Config.EMOJI_IN_HELP1 or "♦️"
python_emoji2 = Config.EMOJI_IN_HELP2 or "♦️"
alive_emoji = Config.ALIVE_EMOJI or "⚜"
python_pic = Config.PM_PIC or "https://te.legra.ph/file/0c605739ddaa472cad75f.jpg"
cstm_pmp = Config.PM_MSG
ALV_PIC = Config.ALIVE_PIC
help_pic = Config.HELP_PIC 
VAR_PIC = Config.ALIVE_PIC
PREV_REPLY_MESSAGE = {}
mybot = Config.BOT_USERNAME
COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r".")
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"

LOG_GP = Config.LOGGER_ID
mssge = (
    str(cstm_pmp)
    if cstm_pmp
    else "**You Have Trespassed To My Master's PM!\nThis Is Illegal And Regarded As Crime.**"
)
TOTAL_WARN = Config.MAX_FLOOD_IN_PM
USER_BOT_WARN_ZERO = "Enough Of Your Flooding In My Master's PM!! \n\n**🚫 Blocked and Reported**"

PYTHON_FIRST = (
    "__{}__\nPlease choose why u are here.♥️!!"
)



var_txt = """
     ♦️ALL VAR♦️
•ALIVE_NAME = `{}`
•ALIVE_MSG = `{}`
•ABUSE = {}
•ASSISTANT = {}
•AWAKE_PIC = `{}`
•BOT_USERNAME = `{}`
•BOT_TOKEN = `{}`
•EXTRA_PLUGIN = `{}`
•OP_PIC = `{}`
•PM_DATA = {}
•PM_PIC = `{}`
•LOGGER_ID = `{}`
"""




alive_txt = """
**{}**\n"
**╔════❰🐍 Ⲃⲟⲧ Ⲓⲛϝⲟʀⲙⲁⲧⲓⲟⲛ🐍 ❱═❍⊱❁۪۪¤๋͜\n"
**║╭━━━━━━━━━━━━━━━➣ \n"
**║┣⪼Developer^By┣⪼ [Legend-Lx](t.me/Legendl_Mr_Hacker) \n"
**║┣⪼Edition^Developer^By ┣⪼ [Legend-Os](t.me/The_LegendBoy) \n"
**║⪼ Ⲟⲱⲛⲉʀ     ┣⪼ [ℓєgєи∂-ℓx](t.me/Legendl_Mr_Hacker) \n"
**║┣⪼ Ⲋⲧⲁⲧυⲋ      ┣⪼ Ⲟⲛⳑⲓⲛⲉ\n"
**║┣⪼ Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ ┣⪼ {mention}\n"
**║┣⪼Ⳙⲣⲧⲓⲙⲉ      ┣⪼  {uptime}\n"
**║┣⪼Ⲃⲟⲧ Ⲣⲓⲛⳋ     ┣⪼  {uptime}\n"   
**║┣⪼Ⲣⲩⲧⲏⲟⲛ       ┣⪼  {PYTHONversion}\n"
**║┣⪼Os:        ┣⪼   Kali GNU/Linux Rolling x86_64 \n"   
**║┣⪼Ⲧⲉⳑⲉⲧⲏⲟⲛ     ┣⪼  {version.__version__}\n" 
**║⪼[✨🐍PYTHON┣⪼ 𝐔𝐬𝐞𝐫𝐛𝐨𝐭🐍✨](https://t.me/Python_Userbot_Support)\n"
**║╰━━━━━━━━━━━━━━━➣
**╚══════════════════❍⊱❁۪۪¤๋͜-  \n"
"""

def button(page, modules):
    Row = python_row
    Column = 3

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, pyt(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(f"{python_emoji1} " + pair + f" {python_emoji2}", data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
               f"⭅ɮǟƈӄ", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"🔥 Close 🔥", data="close"
            ),
            custom.Button.inline(
               f"ռɛӼȶ⭆", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]


    modules = CMD_HELP
if Config.BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "pythonbot_help":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            help_msg = f"🔥『{python_mention}』🔥\n\n"
            **║┣⪼🔥𝚃𝚘𝚝𝚊𝚕 𝙼𝚘𝚍𝚞𝚕𝚎𝚜 𝙸𝚗𝚜𝚝𝚊𝚕𝚕𝚎𝚍🔥⭆**`{led(CMD_HELP)}`\n"
            **║┣⪼🔥Tοταℓ Cοммαи∂ѕ🔥⭆** `{led(apn)}`\n"
            **║┣⪼🔥Pαցҽ🔥⭆**1/{veriler[0]}\n" 
           
            if help_pic and help_pic.endswith((".jpg", ".png")):
                result = builder.photo(
                    help_pic,
                    text=help_msg,
                    buttons=veriler[1],
                    link_preview=False,
                )
            elif help_pic:
                result = builder.document(
                    help_pic,
                    text=help_msg,
                    title="Help Menu",
                    buttons=veriler[1],
                    link_preview=False,
                )
            else:
                result = builder.article(
                    f"Hey! Only use .op please",
                    text=help_msg,
                    buttons=veriler[1],
                    link_preview=False,
                )
        elif event.query.user_id == bot.uid and query == "alive":
            pyt_hon = alive_txt.format(Config.ALIVE_MSG, alive_emoji, python_mention, alive_emoji,  PYTHONversion, alive_emoji, version.__version__, alive_emoji, Developer^By, alive_emoji, Edition^Developer^By, alive_emoji,Ⲟⲱⲛⲉʀ ,alive_emoji, Ⲋⲧⲁⲧυⲋ , alive_emoji, Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ ,alive_emoji ,Ⳙⲣⲧⲓⲙⲉ ,alive_emoji ,Ⲣⲩⲧⲏⲟⲛ ,alive_emoji  ,Os ,alive_emoji  ,Ⲧⲉⳑⲉⲧⲏⲟⲛ ,alive_emoji
            alv_btn = [
                [Button.url(f"{PYTHON_USER}", f"tg://openmessage?user_id={Legendl_Mr_Hacker}")],
                [Button.url("❣My Channel❣", f"https://t.me/{my_channel}"), 
                Button.url("💝My Group💝", f"https://t.me/{my_group}")],
            ]
            if ALV_PIC and ALV_PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALV_PIC,
                    text=pyt_hon,
                    buttons=alv_btn,
                    link_preview=False,
                )
            elif ALV_PIC:
                result = builder.document(
                    ALV_PIC,
                    text=pyt_hon,
                    title="PythonBot Alive",
                    buttons=alv_btn,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    text=pyt_end,
                    title="PythonBot Alive",
                    buttons=alv_btn,
                    link_preview=False,
                )
        elif event.query.user_id == bot.uid and query == "fsub":
            fsub_btn = [
                [Button.url(f"{PYTHON_USER}", f"tg://openmessage?user_id={Legendl_Mr_Hacker}")],
                [Button.url("📍My Channel📍", f"https://t.me/{my_channel}"), 
                Button.url("💝My Group💝", f"https://t.me/{my_group}")],
            ]
            if ALV_PIC and ALV_PIC.endswith((".jpg", ".png")):
                result = builder.article(
                    buttons=fsub_btn,
                    link_preview=False,
                )
            elif ALV_PIC:
                result = builder.document(
                    buttons=fsub_btn,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    buttons=alv_btn,
                    link_preview=False,
                )
        
        elif event.query.user_id == bot.uid and query == "pm_warn":
            pyth_on = PYTHON_FIRST.format(mssge)
            result = builder.photo(
                file=python_pic,
                text=pyth_on,
                buttons=[
                    [
                        custom.Button.inline("📝 Request 📝", data="req"),
                        custom.Button.inline("💬 Chat 💬", data="chat"),
                    ],
                    [custom.Button.inline("🚫 Spam 🚫", data="heheboi")],
                    [custom.Button.inline("Curious ❓", data="pmclick")],
                ],
            )

        elif event.query.user_id == bot.uid and query == "varboy":
            py_thon = var_txt.format(Config.ALIVE_NAME, Config.ALIVE_MSG, Config.ABUSE, Config.ASSISTANT, Config.AWAKE_PIC, Config.BOT_USERNAME, Config.BOT_TOKEN, Config.EXTRA_PLUGIN, Config.HELP_PIC, Config.PM_DATA, Config.PM_PIC, Config.LOGGER_ID)
            var_btn = [
                [Button.url(f"{PYTHON_USER}", f"tg://openmessage?user_id={Legendl_Mr_Hacker}")],
                [Button.url("🔹️Command🔹️", f"http://telegra.ph/Astronomer-10-07"),],
            ]
            if VAR_PIC and VAR_PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    VAR_PIC,
                    text=py_thon,
                    buttons=var_btn,
                    link_preview=False,
                )
            elif VAR_PIC:
                result = builder.document(
                    VAR_PIC,
                    text=py_thon,
                    title="PythonBot Alive",
                    buttons=var_btn,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    text=py_thon,
                    title="PythonBot Alive",
                    buttons=var_btn,
                    link_preview=False,
                )
         
        elif event.query.user_id == bot.uid and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"**⚜ 𝙻𝚎𝚐𝚎𝚗𝚍𝚊𝚛𝚢 𝙰𝚏 PYTHONBOT ⚜**",
                buttons=[
                    [Button.url("♥️ Tutorial ♥", "https://youtu.be/9dQgdUJfk_k")], 
                    [Button.url("📍 𝚁𝚎𝚙𝚘 📍", "https://github.com/LEGEND-LX/PYTHONBOT-V9.0.8")],
                    [Button.url("💞 Deploy 💞", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FLEGEND-OS%2FLEGENDBOT&template=https%3A%2F%2Fgithub.com%2FLEGEND-OS%2FLEGENDBOT")],
                ],
            )

        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )

        else:
            result = builder.article(
                "@Python_Userbot_Support",
                text="""**Hey! This is [Pythonẞø†](https://t.me/Python_Userbot_Support) \nYou can know more about me from the links given below 👇**""",
                buttons=[
                    [
                        custom.Button.url("🔥 CHANNEL 🔥", "https://t.me/Python_Userbot_Support"),
                        custom.Button.url(
                            "⚡ GROUP ⚡", "https://t.me/Python_Userbot_Support"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "✨ REPO ✨", "https://github.com/LEGEND-LX/PYTHONBOT-V9.0.8"),
                        custom.Button.url
                    (
                            "🔰 TUTORIAL 🔰", "https://youtu.be/bPzvmaQejNM"
                    )
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"pmclick")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for Other Users..."
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"🔰 This is Pythonẞø† PM Security for {Python_mention} to keep away unwanted retards from spamming PM..."
            )

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"req")))
    async def on_pm_click(python):
        if python.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master {python_mention} Im Try To Get Rid Of This Nigga Pls Dont Touch"
            await python.answer(fck_bit, cache_time=0, alert=True)
            return
        await python.get_chat()
        python_id = python.query.user_id
        await python.edit("Oh You Wanna Talk With My Master\n\nPls Wait Dear \n\n**Btw** **You Can Wait For My Master**")
        await asyncio.sleep(2)
        await python.edit(
            "Which Type Of Request U Want?", buttons= [
            [Button.inline("Register", data="school")],
            [Button.inline("As Usual", data="tg_okay")],
            ], 
        )
        yup_text = "`Warning`-❗️⚠️Don't send any message now wait kindly!!!❗️⚠️"
        await bot.send_message(python.query.user_id, yup_text)
    
    
    
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"tg_okay")))
    async def yeahbaba(python):
            if legend.query.user_id == bot.uid:
                fck_bit = f"Oh! C'mon Master.This Is for other users"
                await python.answer(fck_bit, cache_time=0, alert=True)
            else:
                await python.edit(
                    f"✅ **Request Registered** \n\n{python_mention} will now decide to talk with u or not\n😐 Till then wait patiently and don't spam!!"
                    )
                target = await python.client(GetFullUserRequest(python.query.user_id))
                first_name = html.escape(target.user.first_name)
                ok = python.query.user_id
                if first_name is not None:
                    first_name = first_name.replace("\u2060", "")
                    tosend = f"**👀 Hey {python_mention} !!** \n\n⚜️ You Got A Request From [{first_name}](tg://user?id={ok}) In PM!!"
                    await bot.send_message(LOG_GP, tosend)



    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"school")))
    async def yeahbaba(python):
            if legend.query.user_id == bot.uid:
                fck_bit = f"This Is For Other user"
                await python.answer(fck_bit, cache_time=0, alert=True)
            else:
                await legend.edit(
                    f"✅ **Request Registered** \n\n{legend_mention} will now decide to look for your request or not.\n😐 Till then wait patiently and don't spam!!"
                    )
                target = await legend.client(GetFullUserRequest(event.query.user_id))
                first_name = html.escape(target.user.first_name)
                ok = legend.query.user_id
                if first_name is not None:
                    first_name = first_name.replace("\u2060", "")
                tosend = f"**👀 Hey {legend_mention} !!** \n\n⚜️ You Got A Request From [{first_name}](tg://user?id={ok}) In PM!!"
                await bot.send_message(LOG_GP, tosend)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"chat")))
    async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Ahh!! You here to do chit-chat!!\n\nPlease wait for {legend_mention} to come. Till then keep patience and don't spam."
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**👀 Hey {legend_mention} !!** \n\n⚜️ You Got A PM from  [{first_name}](tg://user?id={ok})  for random chats!!"
            await bot.send_message(LOG_GP, tosend)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"heheboi")))
    async def on_pm_click(legend):
        if legend.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master{legend_mention} Im Try To Get Rid Of This Nigga Pls Dont Touch"
            await legend.answer(fck_bit, cache_time=0, alert=True)
            return
        await legend.get_chat()
        legend_id = legend.query.user_id
        await legend.edit("Okay let Me Think🤫")
        await asyncio.sleep(2)
        await legend.edit("Okay Giving You A Chance🤨")
        await asyncio.sleep(2)
        await legend.edit(
            "Will You Spam?", buttons= [
            [Button.inline("Yes", data="lemme_ban")],
            [Button.inline("No", data="hmm")],
            ],
        )

    
        reqws = "`Warning`- ❗️⚠️Don't send any message now wait kindly!!!❗️⚠️"

        await bot.send_message(legend.query.user_id, reqws)
        await bot.send_message(
            LOG_GP,
            message = f"Hello, Master  [Nibba](tg://user?id={legend_id}). Wants To Request Something.",
            buttons = [Button.url("Contact Him", f"tg://user?id=legend_id")],
        )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hmm")))
    async def yes_ucan(legend):
        if legend.query.user_id == bot.uid:
               lmaoo = "You Are Not Requesting , Lol."
               await legend.answer(lmaoo, cache_time=0, alert=True)
               return          
        await legend.get_chat()
        await asyncio.sleep(2)
        legend_id = legend.query.user_id
        await legend.edit("Okay You Can Wait Till Wait")
        hmmmmm = "Okay Kindly wait  i will inform you"
        await bot.send_message(
                  legend.query.user_id, hmmmmm)
          
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lemme_ban")))
    async def yes_ucan(legend):
        if legend.query.user_id == bot.uid:
               lmaoo = "You Are Not Requesting , Lol."
               await legend.answer(lmaoo, cache_time=0, alert=True)
               return    
        await legend.get_chat()
        await asyncio.sleep(2)
        legend_id = legend.query.user_id
        await legend.edit("Get Lost Retard")
        ban = f"Pahli Fursat Me Nikal\nU Are Blocked" 
        await bot.send_message(
             legend.query.user_id, ban)
        await bot(functions.contacts.BlockRequest(legend.query.user_id))
        await bot.send_message(
                LOG_GP,
                message = f"Hello, Master  [Nibba](tg://user?id={python_id}). Has Been Blocked Due to Choose Spam",
                buttons = [Button.url("Contact Him", f"tg://user?id=python_id")],
            )
       
    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"unmute")))
    async def on_pm_click(event):
        hunter = (event.data_match.group(2)).decode("UTF-8")
        legend = hunter.split("+")
        if not event.sender_id == int(python[0]):
            return await event.answer("This Ain't For You!!", alert=True)
        try:
            await bot(GetParticipantRequest(int(python[1]), int(python[0])))
        except UserNotParticipantError:
            return await event.answer(
                "You need to join the channel first.", alert=True
            )
        await bot.edit_permissions(
            event.chat_id, int(python[0]), send_message=True, until_date=None
        )
        await event.edit("Yay! You can chat now !!")


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"reopen")))
    async def reopn(event):
            if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
                current_page_number=0
                simp = button(current_page_number, CMD_HELP)
                veriler = button(0, sorted(CMD_HELP))
                apn = []
                for x in CMD_LIST.values():
                    for y in x:
                        apn.append(y)
                await event.edit(
                    f"",
                    buttons=simp[1],
                    link_preview=False,
                )
            else:
                reply_pop_up_alert = "This Is For My Master Only.Dont Try To Touch Again. Deploy Ur Own © Pythonẞø†™"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            veriler = custom.Button.inline(f"{python_emoji1} Re-Open Menu {python_emoji2}", data="reopen")
            await event.edit(f"**⚜️ Pythonẞø† Mêñû Prõvîdêr háš běěn čłøšĕd ⚜️**\n\n**Bot Of :**  {python_mention}\n\n            [©️Pythonẞø†]({chnl_link})", buttons=veriler, link_preview=False)
        else:
            reply_pop_up_alert = "κγα υиgℓι καя янє нο мєяє ϐοτ ραя αgαя ϲнαнιγє τοн κнυ∂ κα ϐαиα ℓο иα. Aα נατє нο υиgℓι καяиє мєяє ϐοτ ρє.   ©Pythondẞø†"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
   

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        apn = []
        for x in CMD_LIST.values():
            for y in x:
                apn.append(y)
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                f"🔥『{python_mention}』🔥\n\n"
            **╭━━━━━━━━━━━━━━━➣\n"
            **║┣⪼🔥𝚃𝚘𝚝𝚊𝚕 𝙼𝚘𝚍𝚞𝚕𝚎𝚜 𝙸𝚗𝚜𝚝𝚊𝚕𝚕𝚎𝚍🔥⭆**`{led(CMD_HELP)}`\n"
            **║┣⪼🔥Tοταℓ Cοммαи∂ѕ🔥⭆** `{led(apn)}`\n"
            **║┣⪼🔥Pαցҽ🔥⭆**1/{veriler[0]}\n" 
            **╰━━━━━━━━━━━━━━━➣\n",
                buttons=veriler[1],
                link_preview=False,
            )
        else:
            return await event.answer(
                "This Button Only For My Master.   ©Lêɠêɳ̃dẞø†",
                cache_time=0,
                alert=True,
            )


    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    f"{alive_emoji} " + cmd[0] + f" {alive_emoji}", data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline(f"{legend_emoji1} Help Menu {legend_emoji2}", data=f"page({page})")])
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                f"**📗 𝙵𝚒𝚕𝚎 :**  `{commands}`\n**🔢 Total Commands :**  `{len(CMD_HELP_BOT[commands]['commands'])}`",
                buttons=buttons,
                link_preview=False,
            )
        else:
            return await event.answer(
                "Hoo gya aapka. Kabse tapar tapar dabae jaa rhe h. Khudka bna lo na agr chaiye to. ©Lêɠêɳ̃dẞø†™",
                cache_time=0,
                alert=True,
            )


    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")
        result = f"**📗 𝙵𝚒𝚕𝚎 :**  `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ 𝚆𝚊𝚛𝚗𝚒𝚗𝚐 :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
            result += f"**📍 Type :**  {CMD_HELP_BOT[cmd]['info']['type']}\n\n"
        else:
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ 𝚆𝚊𝚛𝚗𝚒𝚗𝚐 :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**📍 Type :**  {CMD_HELP_BOT[cmd]['info']['type']}\n"
            result += f"**ℹ️ 𝙸𝚗𝚏𝚘 :**  {CMD_HELP_BOT[cmd]['info']['info']}\n\n"
            
        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**🛠 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜 :**  `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
        else:
            result += f"**🛠 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜 :**  `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"
        if command["example"] is None:
            result += f"**💬 𝙴𝚡𝚙𝚕𝚊𝚗𝚊𝚝𝚒𝚘𝚗 :**  `{command['usage']}`\n\n"
        else:
            result += f"**💬 𝙴𝚡𝚙𝚕𝚊𝚗𝚊𝚝𝚒𝚘𝚗 :**  `{command['usage']}`\n"
            result += f"**⌨️ 𝙵𝚘𝚛 𝙴𝚡𝚊𝚖𝚙𝚕𝚎 :**  `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"
            
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                result,
                buttons=[
                    custom.Button.inline(f"{legend_emoji1} Return {legend_emoji2}", data=f"Information[{page}]({cmd})")
                ], 
                link_preview=False,
            )
        else:
            return await event.answer(
                "MY MASTER ONLY CAN ACCESS THIS BUTTON. DEPLOY UR OWN ©Lêɠêɳ̃dẞø†™ ",
                cache_time=0,
                alert=True,
            )

       
