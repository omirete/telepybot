from telepybot import Telepybot

telepybot = Telepybot(token='YOUR_BOT_API_TOKEN')

# Get the info of the webhook we've just setup.
webhook_info = telepybot.webhook.getInfo()
print('IP Address:           ', webhook_info.ip_address)
print('URL:                  ', webhook_info.url)
print('Pending update count: ', str(webhook_info.pending_update_count))
print('Max connections:      ', str(webhook_info.max_connections))
