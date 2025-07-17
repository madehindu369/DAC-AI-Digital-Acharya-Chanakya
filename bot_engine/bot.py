📜 DAC–AI BOT ENGINE (Production Version – Bharatleaks)
Repository: madehindu369/DAC-AI-Digital-Acharya-Chanakya
------------------------------
bot.py (Main Execution Script)
------------------------------
import os import telebot from dotenv import load_dotenv
Load environment variables
load_dotenv() BOT_TOKEN = os.getenv("7501328022:AAHxePvtwhSQRrPI_PQlwNL-zAlzX8UsLjo") CHANNEL_ID = os.getenv("@mbjatadhari")
Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)
Start / Help Command
@bot.message_handler(commands=['start', 'help']) def send_welcome(message): bot.reply_to(message, "🚩 जयतु भारतम्! मैं DAC–AI बॉट हूं – आदेश दें।")
Post Command
@bot.message_handler(commands=['post']) def post_to_channel(message): content = message.text.replace('/post', '').strip() if content: bot.send_message(CHANNEL_ID, content) bot.reply_to(message, "✅ आदेशानुसार संदेश प्रकाशित कर दिया गया।") else: bot.reply_to(message, "❌ संदेश रिक्त है। कृपया /post के बाद सामग्री लिखें।")
Niti Command – send Chanakya Sutra
@bot.message_handler(commands=['niti']) def send_policy(message): policy_quote = ""कृत्येषु धीः, वाक्येषु नीतिरेव बलम्।"\n(कार्य में बुद्धि और वाणी में नीति ही बल है।)" bot.reply_to(message, policy_quote)
Satire Mode Command
@bot.message_handler(commands=['satire']) def send_satire(message): satire = "😏 मूर्खता का उत्तर मौन है; पर जब मौन भी व्यर्थ लगे, तो व्यंग्य करो।" bot.reply_to(message, satire)
Run Bot – Long Polling
bot.infinity_polling()
------------------------------
End of bot.py
------------------------------
------------------------------
requirements.txt
------------------------------
pyTelegramBotAPI python-dotenv
------------------------------
Procfile (for Railway/Render Hosting)
------------------------------
worker: python bot.py
------------------------------
.env.example (Environment Template)
------------------------------
BOT_TOKEN=YOUR_BOT_TOKEN_HERE CHANNEL_ID=@yourchannelusername
------------------------------
README.md (Link Existing Philosophy)
------------------------------
Your existing README philosophy file should remain as project overview.
Link this Bot Engine as: /bot-engine/ folder or direct root deployment.