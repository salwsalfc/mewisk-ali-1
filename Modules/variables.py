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

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

import config
from FallenMusic import BOT_NAME, app


@app.on_message(
    filters.command(["config", "variables"]) | filters.command(["الحاجات","الفارات","الايبهات","كونفنج"],prefixes= ["/", "!","","#"]) & filters.user(config.OWNER_ID)
)
async def get_vars(_, message: Message):
    try:
        await app.send_message(
            chat_id=int(config.OWNER_ID),
            text=f"""<u>𓆘𓆘{BOT_NAME} ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs :𓆘𓆘</u>

𓆘𓆘ايبي ايدي :𓆘𓆘 `{config.API_ID}`
𓆘𓆘ايبي هاش :𓆘𓆘 `{config.API_HASH}`

𓆘𓆘توكن البوت :𓆘𓆘 `{config.BOT_TOKEN}`
𓆘𓆘حد المدة :𓆘𓆘 `{config.DURATION_LIMIT}`

𓆘𓆘ايدي المالك :𓆘𓆘 `{config.OWNER_ID}`
𓆘𓆘سودو يوزر :𓆘𓆘 `{config.SUDO_USERS}`

𓆘𓆘بنج :𓆘𓆘 `{config.PING_IMG}`
𓆘𓆘بدأ :𓆘𓆘 `{config.START_IMG}`
𓆘𓆘جروب الدعم :𓆘𓆘 `{config.SUPPORT_CHAT}`

𓆘𓆘الجلسة :𓆘𓆘 `{config.SESSION}`""",
            disable_web_page_preview=True,
        )
    except:
        return await message.reply_text("𓅽 فشل في إرسال متغيرات التكوين .")
    if message.chat.type != ChatType.PRIVATE:
        await message.reply_text(
            "𓅽 ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘᴍ, ɪ'ᴠᴇ sᴇɴᴛ ᴛʜᴇ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs ᴛʜᴇʀᴇ."
        )
