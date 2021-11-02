from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""♦ **Bem vindo {message.from_user.mention()} !**\n
📝 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **Como você já sabe, sou um bot de tocar músicas e vídeos na call!**

♦ **Descubra todos os comandos do Bot e como eles funcionam clicando no » 🧐 Botão de comandos!**

♦️ **Para saber como usar este bot, clique no » ❓ Botão guia básico!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Adicione-me ao seu grupo ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Guia Básico", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("🧐 Comandos", callback_data="cbcmds"),
                    InlineKeyboardButton("❤️ Pae", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Grupo Oficial", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Canal Oficial", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "👑 Criador", url="https://t.me/xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🧐 Grupo", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "📣 Canal", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**E ae fi de rapariga {message.from_user.mention()}, Eu sou seu pai 😎 {BOT_NAME}**\n\n♦️ Bot está funcionando normalmente\n👑 Meu Mestre fiatin: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ Bot na versão: `v{__version__}`\n♦️ Pyrogram Versão: `{pyrover}`\n♦️ Python Versão: `{__python_version__}`\n♦️ PyTgCalls versão: `{pytover.__version__}`\n♦️ Online Status: `{uptime}`\n\n**Obrigado fi da peste para me adicionar aqui, para reproduzir vídeo & música em seu bate-papo de vídeo grupo** 😭❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("😎👑 `PONG MINHA HOLA, AQUI É PLOC PLOC NO JUREG DELA!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "♦️ bot status:\n"
        f"♦️ **Uptime:** `{uptime}`\n"
        f"♦️ **Tempo que está online:** `{START_TIME_ISO}`"
    )
