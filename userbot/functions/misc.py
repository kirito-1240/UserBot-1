from userbot import app, bot
from userbot.database import DB

async def add_info_to_db():
    app_info = await app.get_me()
    bot_info = await bot.get_me()
    DB.set_key("OWNER_ID" , str(app_info.id))
    DB.set_key("OWNER_NAME" , str(app_info.first_name))
    if app_info.username:
        DB.set_key("OWNER_USERNAME" , str(app_info.username))
    DB.set_key("ASSISTANT_ID" , str(bot_info.id))
    DB.set_key("ASSISTANT_NAME" , str(bot_info.first_name))
    DB.set_key("ASSISTANT_USERNAME" , str(bot_info.username))
