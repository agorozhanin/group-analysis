from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dynaconf import Dynaconf
from telethon import TelegramClient

cfg = Dynaconf(
    envvar_prefix="TL",
    settings_files=['conf.yml', './conf.yml', '.secrets.yml', './.secrets.yml'],
)

BOT = Bot(token=cfg.TOKEN, parse_mode="HTML")
BOT_DISPATCHER = Dispatcher(bot=BOT, storage=MemoryStorage())
TG_CLIENT = TelegramClient('bot', cfg.API_ID, cfg.APP_ID).start(bot_token=cfg.TOKEN)
REPORT_GROUP_ID = cfg.REPORT_GROUP_ID
