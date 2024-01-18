from pyrogram import filters
from pyrogram.types import Message

from BRANDED X KING import app
from BRANDED X KING.core.call import BRANDED

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await BRANDED.stop_stream_force(message.chat.id)
