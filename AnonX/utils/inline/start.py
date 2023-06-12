from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=" ❃𝗔𝗱𝗱 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽❃ ",
                url=f"https://t.me/prayX_musicbot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❃𝗛𝗲𝗹𝗽❃",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝑺𝒆𝒕𝒕𝒊𝒏𝒈𝒔", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=" ❃𝗔𝗱𝗱 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽❃ ",
                url=f"https://t.me/prayit_musicbot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❃𝗛𝗲𝗹𝗽❃", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="❃𝗣𝗿𝗮𝘆❃", url=f"https://t.me/plovestatus"
            )
        ],
     ]
    return buttons

