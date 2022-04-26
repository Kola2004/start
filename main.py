import requests,random,json,os,sys,uuid
import flask
import telebot
from telebot import types
from uuid import uuid4
from user_agent import generate_user_agent
from config import *
import logging
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)
    
idd = str(uuid4())
token = input('Toknen : ')
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def send(message):
	program = types.InlineKeyboardButton(text='DevelopeR',url='https://t.me/MMPMMMM')
	Keyy = types.InlineKeyboardMarkup()
	Keyy.row_width = 2
	Keyy.add(program)
	first = message.chat.first_name
	bot.send_message(message.chat.id,f"*⌯ Hello {first}\n\n⌯ About Bot Sned Rest Instagram\n\n⌯ Send UserName Account Or Email*",parse_mode="markdown",reply_markup=Keyy,reply_to_message_id=message.message_id)
@bot.message_handler(func=lambda m: True)
def Sufi(message):
         user = message.text
         url = "https://i.instagram.com/api/v1/accounts/send_password_reset/"
         headers = {
'Content-Length': '304',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Host': 'i.instagram.com',
'Connection': 'Keep-Alive',
'User-Agent': 'Instagram 6.12.1 Android (29/10; 480dpi; 1080x2255; HUAWEI/HONOR; JSN-L22; HWJSN-H; kirin710; en_US)',
'Cookie2': '$Version=1',
'Accept-Language': 'en-US',
'X-IG-Connection-Type': 'WIFI',
'X-IG-Capabilities': 'AQ==',
'Accept-Encoding': 'gzip',
}
         data = {
"user_email":str(user),
"guid":str(idd),
}
         req = requests.post(url,headers=headers,data=data)
         print(req.text)
         if ('{"obfuscated_email"') in req.text:
         	re=req.text
         	bot.send_message(message.chat.id,f'''- Done Send Rest ✅
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
{re}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
- Tele : @MMPMMMM ''')
         elif ("Please wait a few minutes before you try again.") in req.text:
         	program = types.InlineKeyboardButton(text='DevelopeR',url='https://t.me/MMPMMMM')
         	Keyy = types.InlineKeyboardMarkup()
         	Keyy.row_width = 2
         	Keyy.add(program)
         	bot.send_message(message.chat.id,f'''
❌ Please wait a few minutes before you try again''',reply_markup=Keyy)
         elif ("no-js not-logged-in client-root touch") in req.text:
         	program = types.InlineKeyboardButton(text='DevelopeR',url='https://t.me/MMPMMMM')
         	Keyy = types.InlineKeyboardMarkup()
         	Keyy.row_width = 2
         	Keyy.add(program)
         	bot.send_message(message.chat.id,f'''
❌ Not Send Try With Valid iInformation''',reply_markup=Keyy)
         else:
         	program = types.InlineKeyboardButton(text='DevelopeR',url='https://t.me/MMPMMMM')
         	Keyy = types.InlineKeyboardMarkup()
         	Keyy.row_width = 2
         	Keyy.add(program)
         	bot.send_message(message.chat.id,f'''
❌ Not Send Try With Valid Information''',reply_markup=Keyy)


@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://resddrrr4.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
bot.polling()