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

import asyncio

import speedtest
from pyrogram import filters

from FallenMusic import SUDOERS, app


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("𓆘𓆘⇆ جارٍ تشغيل اختبار سرعة التنزيل...𓆘𓆘")
        test.download()
        m = m.edit("𓆘𓆘⇆ تشغيل اختبار سرعة التحميل...𓆘𓆘")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("𓆘𓆘↻ مشاركة نتائج اختبار السرعة...𓆘𓆘")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(["speedtest", "spt"]) | filters.command(["فحص","السرعة","السرعه","سرعه","سرعة"],prefixes= ["/", "!","","#"]) & SUDOERS)
async def speedtest_function(_, message):
    m = await message.reply_text("𓆘𓆘𓅽 تشغيل اختبار السرعة...𓆘𓆘")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""✯ 𓆘𓆘نتائج اختبار سرعه ࢪيفز𓆘𓆘 ✯
    
<u>𓆘𓆘𓅽 عميل :𓆘𓆘</u>
𓆘𓆘𓅽 مزود خدمة الإنترنت :𓆘𓆘 {result['client']['isp']}
𓆘𓆘𓅽 الدولة :𓆘𓆘 {result['client']['country']}
  
<u>𓆘𓆘𓅽 سيرفر :𓆘𓆘</u>
𓆘𓆘𓅽 الاسم :𓆘𓆘 {result['server']['name']}
𓆘𓆘𓅽 الدولة :𓆘𓆘 {result['server']['country']}, {result['server']['cc']}
𓆘𓆘𓅽 راعي :𓆘𓆘 {result['server']['sponsor']}
𓆘𓆘𓅽 وقت الإستجابة :𓆘𓆘 {result['server']['latency']}  
𓆘𓆘𓅽 البنج :𓆘𓆘 {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()
