import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "𝐂𝐚𝐥𝐥 𝐕𝐢𝐝𝐞𝐨 𝐌𝐮𝐬𝐢𝐜")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx")
ALIVE_NAME = getenv("ALIVE_NAME", "Baianor dos infernu")
BOT_USERNAME = getenv("BOT_USERNAME", "Call_Video_Musicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Assistant_Grave_Sad_Official")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "blazer808_Stay")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "GR4V3_S4D_CRAZZY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! _ .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/8ab6b696c801767fcf14e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9999999999"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/19ef76c0a097b1a394b00.png")
