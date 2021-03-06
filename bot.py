import os, logging, asyncio
import random
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

# ÆkmÉ OÄlum...!!!
emj = ['ð','ð¥°','ð','ð®âð¨','ð','ð¾','ð¤¡','ð¥³','ð»','ð¼','ð½','ð','ð¸','ð¤´','ðð»','ð¤¶','ð§ââï¸','ð§','ð§ââï¸','ð§ââï¸','ð§','ð§ââï¸','ð§','ð','ð','ð¶','ð¶','ð±','ð­','ð¹','ð°','ð¦','ð»','ð¼','ð¨','ð¯','ð¦','ð®','ð·','ð½','ð¸','ðµ','ð','ð','ð','ð','ð£','ð¥','ð¦','ð','ð¦','ð','ð','ð¹','ð¥','ðº','ð¸','ð¼','ð»','â­ï¸','ð','â¨','â¡ï¸','ð¥','ð','âï¸','ð«','ð','ðº','ð«','ð','â','ð§¸','ð¦','ð©âð¦°','ð®','âï¸','ð','ð¦','ð¨ð»ââï¸','ð¥¶','ð¿','ð','ð','ð','â¥ï¸','â¤ï¸âð©¹','ð','ð','ð','ð','â¤ï¸âð¥','ð¤','â¡','ð','ð¤¡','ð','ð¥','ð¼','ð¤','â','ð©âð¨','ð§','ð¼','ð','ð¹','ð¥','ð·','ðº','ð¸','ðµï¸','ð»','ð','ð','ð¾','ð±','ð¿','ð','âï¸','ð','ðµ','ð´','ð³','ð²','ðï¸','ðªï¸','âï¸','â','âï¸','ðï¸','ð','ð','ð¤¶','ð©âð¼','ð§','ð§','ð','ðº','ð©âð¦°','ðª','ð¦','ð¢','ð','ð¤','ð£','ð¥','ð¦','ð','ðï¸','ð¦¢','ð¦©','ð¦','ð¬','ð','ð³','ð','ð ','ð¦','ð¡','ð¦','ð¦','ð¦','ð¦','ð','ð¦','ð·ï¸','ð¸ï¸','ð','ð¦','ð¦','ð','ð','ð¾','ð','ð','ð','ð','ð','ð¥­','ð','ð','ð','ð¥','ð','ð¥¥','ð¶ï¸','ð','ð','ð§','ð¥','ð¦','ð§','ð¨','ð¦','ð¥§','ð°','ð®','ð','ð§','ð­','ð¬','ð©','ðº','ð»','ð¥','ð¾','ð·']
# ÆkmÉ OÄlum...!!!

@client.on(events.NewMessage(pattern='^(?i)/dur'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**TSK Emtag Bot.**, Qrupda vÉ ya kanalda demÉk olar ki, hÉr bir Ã¼zvÃ¼ qeyd edÉ bilÉrÉm ð¤\nDaha ÉtraflÄ± mÉlumat Ã¼Ã§Ã¼n **/help**'yazÄ±n.",
                    buttons=(
                      [Button.url('â Gurup EklÉ', 'http://t.me/TskEmojiTagBot?startgroup=a'),
                      Button.url('âï¸ Kanal', 'https://t.me/TSK_resmi'),
                      Button.url('ð¨ð»âð» Sahibim', 'https://t.me/Muratdida')]
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**TSK Emtag Bot.'un KÃ¶mÉk Menyusu**\n\nÆmirlÉr: /tag \nBu Émri baÅqalarÄ±na demÉk istÉdiyiniz mÉtnlÉ birlikdÉ istifadÉ edÉ bilÉrsiniz. \nEmoji tag: /etag'Bu Émri cavab olaraq istifadÉ edÉ bilÉrsiniz. istÉnilÉn mesaj Bot istifadÉÃ§ilÉri cavab mesajÄ±na iÅarÉlÉyÉcÉk"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('â Gurup EklÉ', 'http://t.me/TskEmojiTagBot?startgroup=a'),
                       Button.url('âï¸ Kanal', 'https://t.me/TSK_resmi'),
                      Button.url('ð¨ð»âð» Sahibim', 'https://t.me/Muratdida')]
                    ),
                    link_preview=False
                   )


@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__YalnÄ±zca yÃ¶neticiler hepsinden bahsedebilir!__")
   
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:

    return await event.respond("__YalnÄ±zca yÃ¶neticiler hepsinden bahsedebilir!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__MÉn kÃ¶hnÉ mesajlar Ã¼Ã§Ã¼n Ã¼zvlÉri qeyd edÉ bilmÉrÉm! (qrupa ÉlavÉ edilmÉzdÉn ÉvvÉl gÃ¶ndÉrilÉn mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__mÉnÉ arqument ver!__")
  else:
    return await event.respond("__YalnÄ±zca yÃ¶neticiler hepsinden bahsedebilir!__")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Durdum ð¤")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Durdum ð¤")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

# Emoji Modulu (aykhan_s) .
@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def etag(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bu Émr qruplarda vÉ kanallarda istifadÉ edilÉ bilÉr!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__BÃ¼tÃ¼n bunlar haqqÄ±nda yalnÄ±z idarÉÃ§ilÉr danÄ±Åa bilÉr!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("K__Ã¶hnÉ yazÄ±lar Ã¼Ã§Ã¼n Ã¼zvlÉri qeyd edÉ bilmÉrÉm! (qrupa ÉlavÉ edilmÉzdÉn ÉvvÉl gÃ¶ndÉrilÉn mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__mÉnÉ arqument ver!__")
  else:
    return await event.respond("BaÅqalarÄ±nÄ± qeyd etmÉk Ã¼Ã§Ã¼n mesaja cavab verin vÉ ya mÉnÉ mÉtn yazÄ±n!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emj)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Durdum ð¤")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emj)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Durdum ð¤")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

print(">> Bot rahat Ã§alÄ±ÅÄ±r narahat olmayÄ±n ð @BLACK_MMC MÉlumat ala bilÉrsiniz <<")
client.run_until_disconnected()
