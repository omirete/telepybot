from telepybot import Telepybot

telepybot = Telepybot(token='YOUR_BOT_API_TOKEN')

user_id = 'USER_ID_OF_THE_CONTACT_TO_SEND_A_MESSAGE_TO'

telepybot.sendMsg(user_id, 'This message was sent using Telepybot!')
