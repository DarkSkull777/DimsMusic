from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>hey {message.from_user.first_name}, Saya Adalah {bn}\n
Saya Bot Music Group, Yang dapat Memutar Lagu di Voice Chat Group Dengan cara yang Mudah
Saya Memiliki Banyak Fitur Praktis Seperti :
┏━━━━━━━━━━━━━━
┣• Memutar Musik.
┣• Mendownload Lagu.
┣• Mencari Lagu Yang ingin di Putar atau di Download.
┗━━━━━━━━━━━━━━ 
❃ Managed With 🔥 By : @xskull7
━━━━━━━━━━━━━━━\n 
Asisten harus ada di grup Anda untuk memutar musik di obrolan suara grup Anda.\n 
untuk mengetahui perintah saya tekan /help</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "WEBSITE📌", url="https://darkskull7.my.to"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ASISTEN🤖", url="https://t.me/xskull77"
                    ),
                    InlineKeyboardButton(
                        "BLOG🌹", url="https://darkskull7.blogspot.com"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Tambahkan Ke Group⚡️", url="https://t.me/dimasvcmusic_bot?startgroup=true"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
