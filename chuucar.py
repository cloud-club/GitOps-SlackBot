import json
import slack_sdk
from datetime import date

# token : xoxb-4318076994242-4360939404208-xS4HHYEQYOiOh1qkAIprNrgH

SLACK_TOKEN = "xoxb-4318076994242-4360939404208-xS4HHYEQYOiOh1qkAIprNrgH"
SLACK_CHANNEL = "#ch-slackbot-test"

b_day='{"ch": "20000817","yg": "20000207","jw": "19990311","test": "20001110","test2":"11991110"}'
b_dict = json.loads(b_day)

def chuucar_send_msg(slack_msg):
    client = slack_sdk.WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(channel=SLACK_CHANNEL,text=slack_msg)
    
today = date.today()

for key,val in b_dict.items():
    #date_of_birth = date(2022,11,10)    
    date_of_birth = date(int(val[0:4]), int(val[4:6]), int(val[6:8]))
    #print(key,date_of_birth)

    birthday = date(today.year, date_of_birth.month, date_of_birth.day)
    days_until_birthday = (birthday-today).days
    days_alive = (today-date_of_birth).days

    if days_until_birthday == 0:
        chat = "Today is "+ key + "'s Birthday."+" Let's Celebrate Together!!"
        chuucar_send_msg(chat)


