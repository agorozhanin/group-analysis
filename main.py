from aiogram.types import ContentType
from telethon import functions
from aiogram import executor, types, md
from settings import BOT_DISPATCHER, TG_CLIENT, BOT, REPORT_GROUP_ID


async def get_users(client, group_id):
    result_dict = {}
    async for user in client.iter_participants(group_id):
        if not user.deleted:
            full_user = await client(functions.users.GetFullUserRequest(user.id))
            about = full_user.full_user.about
            phone = user.phone
            if about and phone:
                result_dict[str(phone)] = str(about)

    return result_dict


START_COMMAND = '&'


@BOT_DISPATCHER.message_handler(content_types=ContentType.TEXT, text=[START_COMMAND])
async def start_command(message: types.Message):
    await message.delete()

    users_info = await get_users(TG_CLIENT, message.chat.id)
    group_link = await message.chat.get_url()

    report_msg = 'Группа: {}\n\n'.format(md.hlink(message.chat.title, str(group_link)))
    for i in users_info:
        report_msg += '\n'.join([i, users_info[i]]) + '\n\n'

    await BOT.send_message(chat_id=REPORT_GROUP_ID, text=report_msg, disable_web_page_preview=True)


# @BOT_DISPATCHER.message_handler(content_types=['new_chat_members'])
# async def join_bot_handler(message: types.Message):


if __name__ == '__main__':
    executor.start_polling(dispatcher=BOT_DISPATCHER)
