import telebot, requests, re
from telebot import types
from bs4 import BeautifulSoup as B
token = "7050017752:AAGMm2Dv9RC3scojzFbVo8irZhdEogrujL8"
bot = telebot.TeleBot(token)
lmage = "https://t.me/ifuwufuj/25"
@bot.message_handler(commands=["start"])
def start(message):
    markup = gen_markup()
    caption = """
👋 ¦ مرحباً بك عزيزي في بوت تنزيل من Happy Mode يمكنك تنزيل الالعاب والتطبيقات المعدله وبكل سهولة كل ماعليك هو ارسال اسم التطبيق او اللعبه الذي تود البحث عنه واعطيك روابط للتنزيل
"""
    bot.send_photo(message.chat.id, lmage, caption=caption, reply_markup=markup)
def gen_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    dev = types.InlineKeyboardButton(text="𝖣𝖤𝖵𝖤𝖫𝖮𝖯𝖤𝖱", url="t.me/lIIHII")
    markup.add(dev)
    app = types.InlineKeyboardButton(text="✓ Search ", callback_data="app")
    markup.add(app)
    return markup
@bot.callback_query_handler(func=lambda call: True)
def searchs(call):
    if call.data == "app":
        bot.send_message(call.message.chat.id, """
⚜️ ¦ يرجى ارسال اسم التطبيق للبحث عليه في Happy Mode 
""") 
    else:
        pass
@bot.message_handler(func=lambda message: True)
def get(message):
    try:
        msg = message.text
        bot.send_message(message.chat.id, f"""
⌛ ¦ تم البحث على {msg}
""")
        h = requests.get(f"https://www.happymod.com/search.html?q={msg}")
        soup = B(h.content, 'html.parser')
        name = soup.find(attrs={"class":"pdt-app-h3"}).text
        url_of_game = soup.find(attrs={"class":"pdt-app-h3"})
        text = url_of_game
        j = "".join(re.findall("href=\"(.*?)\"", str(text)))
        bot.send_message(message.chat.id, f""" 
✅ ¦ تم البحث بنجاح : 
⚖️ ¦\nURL : https://www.happymod.com{j}
🍀 ¦ اسم التطبيق : {name}
⚡ ¦ رابط التحميل : https://www.happymod.com{j}how-does-happymod-work.html 
""")   
    except:
        bot.send_message(message.chat.id, "Error")
bot.polling(True)
