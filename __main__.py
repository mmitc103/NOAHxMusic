import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from NOAHxMusic import LOGGER, app, userbot
from NOAHxMusic.core.call import Hotty
from NOAHxMusic.misc import sudo
from NOAHxMusic.plugins import ALL_MODULES
from NOAHxMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("NOAHxMusic.plugins" + all_module)
    LOGGER("NOAHxMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Hotty.start()
    try:
        await Hotty.stream_call("https://te.legra.ph/file/9c279179b258b3bb9902f.mp4")
    except NoActiveGroupCall:
        LOGGER("NOAHxMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Hotty.decorators()
    LOGGER("NOAHxMusic").info(
        "Congrats! Your music bot is deployed successfully. For queries join @neetxdiscussion"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("NOAHxMusic").info("Stopping NOAH Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
