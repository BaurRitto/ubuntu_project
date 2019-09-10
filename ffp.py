from flask import Flask, render_template
import telegram
#from telebot.credentials import bot_token, bot_user_name,URL
#from telebot.mastermind import get_response

bot_token = "813851707:AAF7OR0gukW38DKLYrBbjmJyiB_SwYg2FJ4"
bot_user_name = "ffp_project_bot"
URL = "104.248.4.159"

bot = telegram.Bot(token=bot_token)

app = Flask(__name__)

@app.route("/hello")
def hello():
	return render_template('home.html')
if __name__ == "__main__":
	app.run(host= "104.248.4.159",debug=True) 
 

@app.route('/{}'.format(bot_token), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
	update = telegram.Update.de_json(request.get_json(force=True), bot)
	chat_id = update.message.chat.id
	msg_id = update.message.message_id
	text = update.message.text.encode('utf-8').decode()
	print("got text message :", text)
	bot.sendMessage(chat_id=chat_id, text=text, reply_to_message_id=msg_id)
	return 'ok'

@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

