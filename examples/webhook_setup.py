from telepybot import Telepybot

telepybot = Telepybot(token='YOUR_BOT_API_TOKEN')

telepybot.webhook.autosetup(webhook_location='bots/telegram')

# Get the info of the webhook we've just setup.
webhook_info = telepybot.webhook.getInfo()

print('\nTelegram will now forward all messages received by the bot to the following URL using a POST request. 👇')
print(webhook_info.url)
