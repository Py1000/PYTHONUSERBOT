from userbot import *
from PYTHONBOT.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

#-------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "PYTHON"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

python = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={python})"


PM_IMG = "https://telegra.ph/file/00399ad38373f61c5a2ff.jpg"
pm_caption ="**PythonαΊΓΈβοΈ πΈπ πΎπππππ**\n\n"

pm_caption += f"**βββοΈβ οΈβtΝαΊΜΈ PythonαΊΓΈβοΈβ οΈβββ**\n"
pm_caption += f"**β£π₯ πΌπ’ πΌπππππ    : {mention}**\n"
pm_caption += f"**β£π₯ ππππππππ : `{version.__version__}`**\n"
pm_caption += f"**β£π₯ PYTHONBOT : {PYTHONversion}**\n"
pm_caption += f"**β£π₯ ππππ     : `{sudou}`**\n"
pm_caption += f"**β£π₯ πΎπ πππ     : [Legend-Lx](https://t.me/Legendl_Mr_Hacker)**\n"
pm_caption += f"**ββββββ[β οΈπΆππππβ οΈ](https://t.me/Python_Userbot_Support)βββββββββ**\n"

pm_caption += "    [β οΈΡΡΟΞΏβ οΈ](https://github.com/LEGEND-LX/PYTHONBOT-V9.0.8) πΉ [πβΞΉΟ²ΡΠΈΡΡπ](https://github.com/LEGEND-LX/PYTHONBOT/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="pybot$"))
@bot.on(sudo_cmd(pattern="pybot$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("botalv").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'bot', None, 'Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg'
).add_info(
  'Are u alive?'
).add()
