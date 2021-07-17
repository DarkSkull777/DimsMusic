from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""Perintah dan penggunaannya dijelaskan di sini🔥
**Perintah Untuk Member**

- `/play <Judul Lagu>` - Putar Lagu Yang Anda Minta

- `/dplay <Judul Lagu>` - Putar Lagu Yang Anda Minta Melalui Deezer

- `/splay <Judul Lagu>` - Putar Lagu Yang Anda Minta Melalui Saavn

- `/playlist` - Melihat Daftar Lagu

- `/current` - Melihat Lagu Yang Sedang Di Putar

- `/song <Judul Lagu>` - Download Lagu Yang Anda inginkan dengan cepat

- `/search <query>` - Cari Video Di YouTube Dengan Detail

- `/deezer <Judul Lagu>` - Download Lagu Yang Anda Inginkan Dengan Cepat Melalui Dengan Via Deezer

- `/saavn <Judul Lagu>` - Download Lagu Yang Anda Inginkan Dengan Cepat Melalui Dengan Via Saavn

- `/video <Judul Lagu>` - Download Lagu Yang Anda Inginkan Dengan Cepat

**Admins only**
- `/player` - Buka Panel Pengaturan Pemutar Musik

- `/pause` - Jeda Pemutaran Lagu

- `/resume` - Melanjutkan Pemutaran Lagu

- `/skip` - Memutar Lagu Berikutnya

- `/end` - Hentikan Pemutaran Musik

- `/userbotjoin` - Mengundang asisten ke Grup Anda

- `/userbotleave` - Hapus asisten dari Grup Anda

- `/admincache` - Refresh Daftar Admin""")

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""Perintah dan penggunaannya dijelaskan di sini🔥
**Perintah Untuk Member**

- `/play <Judul Lagu>` - Putar Lagu Yang Anda Minta

- `/dplay <Judul Lagu>` - Putar Lagu Yang Anda Minta Melalui Deezer

- `/splay <Judul Lagu>` - Putar Lagu Yang Anda Minta Melalui Saavn

- `/playlist` - Melihat Daftar Lagu

- `/current` - Melihat Lagu Yang Sedang Di Putar

- `/song <Judul Lagu>` - Download Lagu Yang Anda inginkan dengan cepat

- `/search <query>` - Cari Video Di YouTube Dengan Detail

- `/deezer <Judul Lagu>` - Download Lagu Yang Anda Inginkan Dengan Cepat Melalui Dengan Via Deezer

- `/saavn <Judul Lagu>` - Download Lagu Yang Anda Inginkan Dengan Cepat Melalui Dengan Via Saavn

- `/video <Judul Lagu>` - Download Lagu Yang Anda Inginkan Dengan Cepat

**Admins only**

- `/player` - Buka Panel Pengaturan Pemutar Musik

- `/pause` - Jeda Pemutaran Lagu

- `/resume` - Melanjutkan Pemutaran Lagu

- `/skip` - Memutar Lagu Berikutnya

- `/end` - Hentikan Pemutaran Musik

- `/userbotjoin` - Mengundang asisten ke Grup Anda

- `/userbotleave` - Hapus asisten dari Grup Anda

- `/admincache` - Refresh Daftar Admin""")
