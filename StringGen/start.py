# Authored By Certified Coders — v1.2 (2025-11-14)
import logging
from typing import Union
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from StringGen.save_user import save_user
from StringGen.database import users

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def command_filter(cmd: Union[str, list]) -> filters.Filter:
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(command_filter(["start", "help"]))
async def start_handler(bot: Client, message: Message):
    user = message.from_user
    try:
        await save_user(user)
    except Exception:
        pass

    try:
        bot_info = await bot.get_me()
        bot_name = bot_info.first_name or "This Bot"

        join_info = ""
        if users is not None:
            try:
                existing = await users.find_one({"_id": user.id})
                if existing and "joined" in existing:
                    join_time = existing["joined"]
                    if isinstance(join_time, datetime):
                        join_info = f"\n🕒 ʏᴏᴜ ᴊᴏɪɴᴇᴅ: **{join_time.strftime('%d-%m-%Y %I:%M %p')} IST**"
            except Exception:
                pass

        name = user.first_name or "User"

        response_text = (
            f"👋 ʜᴇʏ {name},\n\n"
            f"ɪ ᴀᴍ **{bot_name}** — ᴀ ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.\n"
            "ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴄʀᴇᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴꜱ ꜰᴏʀ **ᴘʏʀᴏɢʀᴀᴍ / ᴛᴇʟᴇᴛʜᴏɴ**, ᴜꜱᴇʀ ᴀɴᴅ ʙᴏᴛ ᴀᴄᴄᴏᴜɴᴛꜱ."
            f"{join_info}\n\n"
            "ᴛᴀᴘ **ʙᴇʟᴏᴡ** ᴛᴏ ʙᴇɢɪɴ ⬇️"
        )

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("⚙️ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ", callback_data="generate")],
            [
                InlineKeyboardButton("💬 ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/CertifiedCoders"),
                InlineKeyboardButton("📢 ᴄʜᴀɴɴᴇʟ", url="https://t.me/CertifiedCodes")
            ]
        ])

        await message.reply_text(
            text=response_text,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )

    except Exception as e:
        logger.exception("⚠️ Error in /start or /help handler:")
        await message.reply_text(
            f"⚠️ Error: `{str(e)}`\n\nPlease try again later."
        )
