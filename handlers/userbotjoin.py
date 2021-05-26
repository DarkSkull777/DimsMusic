from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Tambahkan saya sebagai admin grup Anda dengan izin penuh kecuali opsi Admin Anonim terlebih dahulu dan harus Memeriksa. /help</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "Dims Music"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"Saya bergabung di sini seperti yang Anda minta")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Assistant sudah ada di obrolan Anda</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} tidak dapat bergabung dengan grup Anda karena banyaknya permintaan bergabung untuk userbot! Pastikan pengguna tidak dilarang dalam grup."
            "\n\nAtau tambahkan @AssistantDims ke Grup Anda secara manual dan coba lagi</b>",
        )
        return
    await message.reply_text(
            "<b>Asisten userbot bergabung dengan obrolan Anda</b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Pengguna tidak dapat meninggalkan grup Anda!."
            "\n\nAtau Kick saya secara manual dari Grup Anda</b>",
        )
        return
