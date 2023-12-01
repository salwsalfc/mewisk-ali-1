# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import platform
import re
import socket
import uuid
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls.__version__ import __version__ as pytgver

from FallenMusic import BOT_NAME, SUDOERS, app
from FallenMusic.Modules import ALL_MODULES


@app.on_message(filters.command(["stats", "sysstats"]) | filters.command(["الحاله","الاحصائيات"],prefixes= ["/", "!","","#"]) & SUDOERS)
async def sys_stats(_, message: Message):
    sysrep = await message.reply_text(
        f"ɢᴇᴛᴛɪɴɢ {BOT_NAME} sʏsᴛᴇᴍ sᴛᴀᴛs, ɪᴛ'ʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ..."
    )
    try:
        await message.delete()
    except:
        pass
    sudoers = len(SUDOERS)
    mod = len(ALL_MODULES)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    architecture = platform.machine()
    processor = platform.processor()
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    sp = platform.system()
    ram = str(round(psutil.virtual_memory().total / (1024.0𓆘𓆘3))) + " ɢʙ"
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}ɢʜᴢ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}ᴍʜᴢ"
    except:
        cpu_freq = "ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0𓆘𓆘3)
    total = str(total)
    used = hdd.used / (1024.0𓆘𓆘3)
    used = str(used)
    free = hdd.free / (1024.0𓆘𓆘3)
    free = str(free)
    platform_release = platform.release()
    platform_version = platform.version()

    await sysrep.edit_text(
        f"""
𓅽 <u>𓆘𓆘{BOT_NAME} احصائيات النظام 𓆘𓆘</u>

𓆘𓆘بايثون :𓆘𓆘 {pyver.split()[0]}
𓆘𓆘بايروجرام :𓆘𓆘 {pyrover}
𓆘𓆘مكالمات بي تي جي :𓆘𓆘 {pytgver}
𓆘𓆘سودورز :𓆘𓆘 `{sudoers}`
𓆘𓆘الوحدات :𓆘𓆘 `{mod}`

𓆘𓆘الايبي :𓆘𓆘 {ip_address}
𓆘𓆘ماك :𓆘𓆘 {mac_address}
𓆘𓆘اسم المضيف :𓆘𓆘 {hostname}
𓆘𓆘منصة :𓆘𓆘 {sp}
𓆘𓆘المعالج :𓆘𓆘 {processor}
𓆘𓆘بنيان :𓆘𓆘 {architecture}
𓆘𓆘إصدار المنصة :𓆘𓆘 {platform_release}
𓆘𓆘إصدار المنصة :𓆘𓆘 {platform_version}

        <b><u>sᴛᴏʀᴀɢᴇ</b><u/>
𓆘𓆘متاح :𓆘𓆘 {total[:4]} ɢɪʙ
𓆘𓆘مستخدم :𓆘𓆘 {used[:4]} ɢɪʙ
𓆘𓆘حر :𓆘𓆘 {free[:4]} ɢɪʙ

𓆘𓆘رام :𓆘𓆘 {ram}
𓆘𓆘النوى المادية :𓆘𓆘 {p_core}
𓆘𓆘مجموع النوى :𓆘𓆘 {t_core}
𓆘𓆘تردد وحدة المعالجة المركزية :𓆘𓆘 {cpu_freq}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="مسح",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        ),
    )
